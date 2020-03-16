from loguru import logger

from flexget import plugin
from flexget.entry import Entry
from flexget.event import event
from flexget.task import Task

logger = logger.bind(name='from_task')


class FromTask(object):
    """An input plugin which returns accepted entries from another task."""

    schema = {'type': 'string'}

    def on_task_input(self, task, config):
        subtask_name = config
        subtask_config = task.manager.config['tasks'].get(subtask_name, {})
        # TODO: This seen disabling is sorta hacky, is there a better way?
        subtask_config.setdefault('seen', False)
        input_task = Task(
            task.manager,
            '{}>{}'.format(task.name, subtask_name),
            config=subtask_config,
            # TODO: Do we want to pass other options through?
            options={'allow_manual': True},
            output=task.output,
            session_id=task.session_id,
            priority=task.priority,
        )
        logger.verbose('Running task `{}` as subtask.', subtask_name)
        input_task.execute()
        logger.verbose('Finished running subtask `{}`.', subtask_name)
        # Create fresh entries to reset state and strip association to old task
        return [Entry(e) for e in input_task.accepted]


@event('plugin.register')
def register_plugin():
    plugin.register(FromTask, 'from_task', api_ver=2)
