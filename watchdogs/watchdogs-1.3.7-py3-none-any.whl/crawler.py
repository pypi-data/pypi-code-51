from asyncio import ensure_future, sleep, wait
from datetime import datetime, timedelta
from json import dumps, loads
from typing import Optional, Tuple

from torequests.utils import ttime
from uniparser import Crawler, RuleNotFoundError

from .config import Config
from .models import Database, Task, query_tasks, tasks
from .utils import check_work_time, get_watchdog_result, solo, try_catch


async def crawl(task):
    crawler: Crawler = Config.crawler
    logger = Config.logger
    logger.info(f'Start crawling: {task.name}')
    crawl_result = await crawler.acrawl(task.request_args)

    if isinstance(crawl_result, RuleNotFoundError):
        msg = f'RuleNotFoundError {task.name}: {crawl_result}'
        logger.error(msg)
        result_list = [{"text": msg}]
    elif isinstance(crawl_result, BaseException):
        logger.error(f'Crawl failed {task.name}: {crawl_result}')
        result_list = None
    else:
        if len(crawl_result) == 1:
            # chain result for __request__ which fetch a new request
            result_list = get_watchdog_result(item=crawl_result.popitem()[1])
            if not isinstance(result_list, list):
                result_list = [result_list]
            # for more log? use force crawl one web UI
            logger.info(f'{task.name} Crawl success: {result_list}' [:150])
        else:
            msg = 'ERROR: crawl_result schema: {rule_name: {"text": "xxx", "url": "xxx"}} or {rule_name: [{"text": "xxx", "url": "xxx"}]}, but given %s' % crawl_result
            logger.error(msg)
            result_list = [msg]
    return task, result_list


async def crawl_once(task_name: Optional[str] = None):
    if task_name is not None:
        return await _crawl_once(task_name)
    with solo:
        result = await try_catch(_crawl_once, task_name)
        return result


async def _crawl_once(task_name: Optional[str] = None):
    """task_name means force crawl"""
    db: Database = Config.db
    now = datetime.now()
    logger = Config.logger
    logger.info(f'crawl_once task_name={task_name} start.')
    # sqlite do not has datediff...
    if task_name:
        query = tasks.select().where(tasks.c.enable == 1).where(
            tasks.c.name == task_name)
    else:
        query = tasks.select().where(tasks.c.enable == 1).where(
            tasks.c.next_check_time <= now)
    todo = []
    now = datetime.now()
    update_query = 'update tasks set `last_check_time`=:last_check_time,`next_check_time`=:next_check_time where task_id=:task_id'
    update_values = []
    CLEAR_CACHE_NEEDED = False
    async for _task in db.iterate(query=query):
        task = Task(**dict(_task))
        # check work hours
        ok, next_check_time = find_next_check_time(task.work_hours or '0, 24',
                                                   task.interval, now)
        if task_name:
            # always crawl for given task_name
            ok = True
        if ok:
            t = ensure_future(crawl(task))
            # add task_name for logger
            setattr(t, 'task_name', task.name)
            todo.append(t)
        # update next_check_time
        values = {
            'last_check_time': now,
            'next_check_time': next_check_time,
            'task_id': task.task_id
        }
        # update task variable for callback
        task.__dict__.update(values)
        update_values.append(values)
        if not ok:
            logger.info(
                f'Task [{task.name}] is not on work time, next_check_time reset to {next_check_time}'
            )
    await db.execute_many(query=update_query, values=update_values)
    logger.info(f'crawl_once crawling {len(todo)} valid tasks.')
    if todo:
        done, pending = await wait(todo, timeout=Config.default_crawler_timeout)
        if pending:
            names = [getattr(t, 'name') for t in pending]
            logger.error(f'crawl timeout: {names}')
        ttime_now = ttime()
        changed_tasks = []
        update_counts = 0
        for t in done:
            task, result_list = t.result()
            if result_list is None:
                continue
            # compare latest_result and new list
            # later first, just like the saved result_list sortings
            old_latest_result = loads(task.latest_result)
            # list of dict
            to_insert_result_list = []
            for result in result_list:
                if result == old_latest_result:
                    break
                to_insert_result_list.append(result)
            if to_insert_result_list:
                update_counts += 1
                # new result updated
                CLEAR_CACHE_NEEDED = True
                query = UpdateTaskQuery(task.task_id)
                # JSON
                new_latest_result = dumps(
                    to_insert_result_list[0], sort_keys=True)
                query.add('latest_result', new_latest_result)
                query.add('last_change_time', now)
                old_result_list = loads(task.result_list or '[]')
                # older insert first, keep the newer is on the top
                for result in to_insert_result_list[::-1]:
                    # result is dict, not json string
                    old_result_list.insert(0, {
                        'result': result,
                        'time': ttime_now
                    })
                new_result_list = dumps(old_result_list[:task.max_result_count])
                query.add('result_list', new_result_list)
                logger.info(f'[Updated] {task.name}. +++')
                await db.execute(**query.kwargs)
                task.latest_result = new_latest_result
                task.last_change_time = now
                task.result_list = new_result_list
                changed_tasks.append(task)
        logger.info(
            f'Crawl task_name={task_name} finished. Crawled: {len(done)}, Timeout: {len(pending)}, Update: {update_counts}.{" +++" if update_counts else ""}'
        )
        for task in changed_tasks:
            await Config.callback_handler.callback(task)
    else:
        logger.info(f'Crawl task_name={task_name} finished. 0 todo.')
    if CLEAR_CACHE_NEEDED:
        logger.info('Clear cache for crawling new results.')
        query_tasks.cache_clear()
    if task_name:
        query = tasks.select().where(tasks.c.name == task_name)
        _task = await db.fetch_one(query=query)
        return dict(_task)


class UpdateTaskQuery:
    __slots__ = ('_query', 'values')

    def __init__(self, task_id):
        self._query = []
        self.values = {'task_id': task_id}

    def add(self, key, value):
        self._query.append(f'`{key}`=:{key}')
        self.values[key] = value

    @property
    def set_values(self):
        if self._query:
            return f'set {", ".join(self._query)}'
        else:
            return ''

    @property
    def kwargs(self):
        return {
            'query': f'update tasks {self.set_values} where `task_id`=:task_id',
            'values': self.values
        }


def find_next_check_time(
        work_hours: str,
        interval: int,
        now: Optional[datetime] = None,
) -> Tuple[bool, datetime]:
    '''
Three kinds of format:

        1. Tow numbers splited by ', ', as work_hours:
            0, 24           means from 00:00 ~ 23:59, for everyday
        2. JSON list of int, as work_hours:
            [1, 19]         means 01:00~01:59 a.m.  07:00~07:59 p.m. for everyday
        3. Standard strftime format, as work_days:
            > Split work_hours by '==', then check
                if datetime.now().strftime(wh[0]) == wh[1]
            %A==Friday      means each Friday
            %m-%d==03-13    means every year 03-13
            %H==05          means everyday morning 05:00 ~ 05:59
        4. Mix up work_days and work_hours:
            > Split work_days and work_hours with ';'/'&' => 'and', '|' for 'or'.
            %w==5;20, 24        means every Friday 20:00 ~ 23:59
            [1, 2, 15];%w==5    means every Friday 1 a.m. 2 a.m. 3 p.m., the work_hours is on the left side.
            %w==5|20, 24        means every Friday or everyday 20:00 ~ 23:59
            %w==5|%w==2         means every Friday or Tuesday
    '''
    # find the latest hour fit work_hours, if not exist, return next day 00:00
    now = now or datetime.now()

    ok = check_work_time(work_hours, now)
    if ok:
        # current time is ok, next_check_time is now+interval
        next_check_time = now + timedelta(seconds=interval)
        return ok, next_check_time
    else:
        # current time is not ok
        next_check_time = now
        # time machine to check time fast
        for _ in range(60):
            # check next interval
            next_check_time = next_check_time + timedelta(seconds=interval)
            _ok = check_work_time(work_hours, next_check_time)
            if _ok:
                # current is still False, but next_check_time is True
                break
        return ok, next_check_time


async def background_loop():
    while 1:
        # non-block running, and be constrained by SoloLock class
        ensure_future(try_catch(db_backup_handler))
        ensure_future(try_catch(crawl_once))
        await sleep(Config.check_interval)


async def db_backup_handler():
    logger = Config.logger
    if check_work_time(Config.db_backup_time):
        logger.warning(f'Backup DB start: {Config.db_backup_time}.')
        # may raise solo error
        with solo:
            result = await try_catch(Config.db_backup_function)
        logger.info(f'Backup DB finished: {result!r}')
