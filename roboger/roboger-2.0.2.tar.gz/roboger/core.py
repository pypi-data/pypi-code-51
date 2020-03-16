__author__ = 'Altertech, http://www.altertech.com/'
__copyright__ = 'Copyright (C) 2018-2020 Altertech Group'
__license__ = 'Apache License 2.0'
__version__ = '2.0.2'

import platform
import os
import sys
import importlib
import logging
import threading
import traceback
import sqlalchemy
import yaml
import signal
try:
    import rapidjson as json
except:
    import json
from types import SimpleNamespace
from flask import Flask, request
from concurrent.futures import ThreadPoolExecutor
from sqlalchemy import text as sql

from pathlib import Path

from pyaltt2.crypto import gen_random_str
from pyaltt2.network import parse_host_port
from netaddr import IPNetwork

logging.getLogger('requests').setLevel(logging.CRITICAL)
logging.getLogger('urllib3').setLevel(logging.CRITICAL)

_d = SimpleNamespace(db=None,
                     use_lastrowid=False,
                     parse_db_json=False,
                     pool=None,
                     secure_mode=False,
                     ip_header=None,
                     log_tracebacks=False,
                     limits=None,
                     redis_conn=None)

config = {}
plugins = {}

product = SimpleNamespace(build=None, version=__version__, user_agent='')
system_name = platform.node()

dir_me = Path(__file__).absolute().parents[1].as_posix()

db_lock = threading.RLock()

logger = logging.getLogger('gunicorn.error')
#logging.getLogger('roboger')

default_timeout = 5

default_db_pool_size = 1

default_thread_pool_size = 10

app = Flask('roboger')

g = threading.local()

emoji_code = {
    20: u'\U00002139',
    30: u'\U000026A0',
    40: u'\U0000203C',
    50: u'\U0001F170'
}


class OverlimitError(Exception):
    pass


def set_build(build):
    product.build = build
    product.user_agent = 'Roboger/{} (v{} build {})'.format(
        product.version[:product.version.rfind('.')], product.version,
        product.build)


def safe_run_method(o, method, *args, **kwargs):
    try:
        f = getattr(o, method)
    except:
        return
    logger.debug(f'CORE executing {o.__name__}.{method}')
    f(*args, **kwargs)


def log_traceback():
    if _d.log_tracebacks: logger.debug('CORE ' + traceback.format_exc())


def load(fname=None):

    class ForeignKeysListener(sqlalchemy.interfaces.PoolListener):

        def connect(self, dbapi_con, con_record):
            try:
                dbapi_con.execute('pragma foreign_keys=ON')
            except:
                pass

    logger.info(f'CORE Roboger server {__version__} {product.build}')
    if not fname:
        fname = os.environ.get('ROBOGER_CONFIG')
    if not fname:
        fname = f'{dir_me}/etc/roboger.yml'
    if not Path(fname).exists:
        fname = '/usr/local/etc/roboger.yml'
    logger.debug(f'CORE using config file {fname}')
    with open(fname) as fh:
        config.update(yaml.load(fh.read())['roboger'])
    _d.secure_mode = config.get('secure-mode')
    _d.log_tracebacks = config.get('log-tracebacks')
    _d.limits = config.get('limits')
    if _d.limits:
        import redis
        rhost, rport = parse_host_port(
            _d.limits.get('redis', {}).get('host', 'localhost'), 6379)
        rdb = _d.limits.get('redis', {}).get('db', 0)
        _d.redis_conn = redis.Redis(host=rhost,
                                    port=rport,
                                    db=rdb,
                                    socket_timeout=get_timeout(),
                                    socket_keepalive=True)
        logger.info(
            f'CORE limits feature activated. Redis: {rhost}:{rport} db: {rdb}')
    config['_acl'] = [IPNetwork(h) for h in config['master']['allow']] if \
            config.get('master', {}).get('allow') else None
    masterkey = os.getenv('ROBOGER_MASTERKEY')
    if masterkey:
        config.setdefault('master', {})['key'] = masterkey
    _d.ip_header = config.get('ip-header')
    for plugin in config.get('plugins', []):
        plugin_name = plugin['name']
        try:
            mod = importlib.import_module(
                'roboger.plugins.{}'.format(plugin_name))
        except:
            try:
                mod = importlib.import_module(
                    'roboger-plugin-{}'.format(plugin_name))
            except:
                logger.error(f'CORE unable to load plugin: {plugin_name}')
                log_traceback()
                continue
        try:
            safe_run_method(mod, 'load', plugin.get('config', {}))
        except:
            logger.error(
                f'CORE failed to load plugin configuration for {plugin_name}')
            log_traceback()
        plugins[plugin_name] = mod
        logger.info(f'CORE added plugin {plugin_name}')
    logger.debug('CORE initializing database')
    if config['db'].startswith('sqlite'):
        _d.db = sqlalchemy.create_engine(config['db'],
                                         listeners=[ForeignKeysListener()])
    else:
        pool_size = config.get('db-pool-size', default_db_pool_size)
        _d.db = sqlalchemy.create_engine(config['db'],
                                         pool_size=pool_size,
                                         max_overflow=pool_size * 2)
    _d.use_lastrowid = config['db'].startswith(
        'sqlite') or config['db'].startswith('mysql')
    _d.parse_db_json = config['db'].startswith(
        'sqlite') or config['db'].startswith('mysql')
    logger.debug(f'CORE database {_d.db}')
    get_db()
    thread_pool_size = config.get('thread-pool-size', default_thread_pool_size)
    logger.debug('CORE initializing thread pool for plugins '
                 f'with max size {thread_pool_size}')
    _d.pool = ThreadPoolExecutor(max_workers=thread_pool_size)
    init_db()
    from . import api
    api.init()


def spawn(*args, **kwargs):
    return _d.pool.submit(*args, **kwargs)


def init_db():
    from sqlalchemy import (Table, Column, BigInteger, Integer, Numeric, CHAR,
                            VARCHAR, MetaData, Float, ForeignKey, Index, JSON,
                            Enum)
    import enum

    class LevelMatch(enum.Enum):
        l = 'l'
        g = 'g'
        le = 'le'
        ge = 'ge'
        e = 'e'

    meta = MetaData()
    addr = Table('addr',
                 meta,
                 Column('id',
                        BigInteger().with_variant(Integer, 'sqlite'),
                        primary_key=True,
                        autoincrement=True),
                 Column('a', CHAR(64), nullable=False, unique=True),
                 Index('addr_a', 'a'),
                 Column('active',
                        Numeric(1, 0),
                        nullable=False,
                        server_default='1'),
                 Column('lim_c',
                        Numeric(8, 0),
                        nullable=False,
                        server_default='100'),
                 Column('lim_s',
                        Numeric(12, 0),
                        nullable=False,
                        server_default='10000000'),
                 mysql_engine='InnoDB',
                 mysql_charset='latin1')
    endpoint = Table('endpoint',
                     meta,
                     Column('id',
                            BigInteger().with_variant(Integer, 'sqlite'),
                            primary_key=True,
                            autoincrement=True),
                     Column('addr_id',
                            BigInteger().with_variant(Integer, 'sqlite'),
                            ForeignKey('addr.id', ondelete='CASCADE')),
                     Index('endpoint_addr_id', 'addr_id'),
                     Column('plugin_name', VARCHAR(40), nullable=False),
                     Column('config', JSON, nullable=False),
                     Column('active',
                            Numeric(1, 0),
                            nullable=False,
                            server_default='1'),
                     Column('description', VARCHAR(255), nullable=True),
                     mysql_engine='InnoDB',
                     mysql_charset='utf8mb4')
    subscription = Table('subscription',
                         meta,
                         Column('id',
                                BigInteger().with_variant(Integer, 'sqlite'),
                                primary_key=True,
                                autoincrement=True),
                         Column('endpoint_id',
                                BigInteger().with_variant(Integer, 'sqlite'),
                                ForeignKey('endpoint.id', ondelete='CASCADE')),
                         Index('subscription_endpoint_id', 'endpoint_id'),
                         Column('active',
                                Numeric(1, 0),
                                nullable=False,
                                server_default='1'),
                         Column('location', VARCHAR(255), nullable=True),
                         Column('tag', VARCHAR(255), nullable=True),
                         Column('sender', VARCHAR(255), nullable=True),
                         Column('level',
                                Numeric(2, 0),
                                nullable=False,
                                server_default='20'),
                         Column('level_match',
                                Enum(LevelMatch),
                                nullable=False,
                                server_default='ge'),
                         mysql_engine='InnoDB',
                         mysql_charset='utf8mb4')
    meta.create_all(_d.db)


def get_db():
    with db_lock:
        try:
            g.conn.execute('select 1')
            return g.conn
        except:
            g.conn = _d.db.connect()
            return g.conn


def get_timeout():
    timeout = config.get('timeout')
    return timeout if timeout else default_timeout


def get_app():
    return app


def get_real_ip():
    return request.headers.get(_d.ip_header, request.remote_addr) if \
            _d.ip_header else request.remote_addr


def get_plugin(plugin_name):
    return plugins['plugin_name']


def is_use_lastrowid():
    return _d.use_lastrowid


def is_parse_db_json():
    return _d.parse_db_json


def is_secure_mode():
    return _d.secure_mode


def is_use_limits():
    return _d.limits is not None


def convert_level(level):
    if level in [10, 20, 30, 40, 50]: return level
    elif isinstance(level, str):
        level = level.lower()
        if level.startswith('d'):
            return 10
        elif level.startswith('i'):
            return 20
        elif level.startswith('w'):
            return 30
        elif level.startswith('e'):
            return 40
        elif level.startswith('c'):
            return 50
        else:
            return 20
    else:
        return 20


def send(plugin_name, **kwargs):
    try:
        spawn(_safe_send, plugin_name, plugins[plugin_name].send, **kwargs)
    except KeyError:
        logger.warning(f'API no such plugin: {plugin_name}')
    except AttributeError:
        logger.warning(f'API no "send" method in plugin {plugin_name}')


def _safe_send(plugin_name, send_func, event_id, **kwargs):
    try:
        logger.debug(f'CORE {event_id} sending via {plugin_name}')
        send_func(event_id=event_id, **kwargs)
    except:
        logger.error(
            f'CORE plugin {plugin_name} raised exception, {event_id} not sent')
        log_traceback()


def check_addr_limit(addr, level, size):
    a = addr['a']
    lim_c = addr['lim_c']
    lim_s = addr['lim_s']
    key_c = f'{a}.lim_c'
    key_s = f'{a}.lim_s'
    try:
        try:
            current_c = int(_d.redis_conn.get(key_c))
        except TypeError:
            current_c = 0
        try:
            current_s = int(_d.redis_conn.get(key_s))
        except TypeError:
            current_s = 0
    except Exception as e:
        logger.error(f'CORE Redis error: {e}')
        return
    logger.debug(f'checking limits for {a}, current: '
                 f'{current_c}, size: {current_s}, current msg level: {level}')
    try:
        if current_c >= lim_c:
            logger.info(f'CORE address count overlimit {a} for all priorities')
            raise OverlimitError(
                f'Messages to {a} are limited by {lim_c} per '
                f'{_d.limits["period"]}. Limit has been reached')
        elif current_c >= lim_c - (lim_c / 100 *
                                   _d.limits['reserve']) and level < 30:
            logger.info(f'CORE address count overlimit {a} for low-priority')
            raise OverlimitError(f'Messages to {a} are limited by {lim_c} per '
                                 f'{_d.limits["period"]}, '
                                 f'{_d.limits["reserve"]}% are reserved for '
                                 'WARNING and higher levels')
        if current_s >= lim_s + size:
            logger.info(f'CORE address size overlimit {a} for all priorities')
            raise OverlimitError(
                f'Messages to {a} are limited by {lim_s} bytes per '
                f'{_d.limits["period"]}. Limit has been reached')
        elif current_s >= lim_s - (lim_s / 100 *
                                   _d.limits['reserve']) and level < 30:
            logger.info(f'CORE address size overlimit {a} for low-priority')
            raise OverlimitError(
                f'Messages to {a} are limited by {lim_s} bytes per '
                f'{_d.limits["period"]}, '
                f'{_d.limits["reserve"]}% are reserved for '
                'WARNING and higher levels')
        _d.redis_conn.incr(key_c)
        _d.redis_conn.incr(key_s, size)
    except OverlimitError:
        raise
    except Exception as e:
        logger.error(f'CORE check limit error: {e}')
        log_traceback()


def reset_addr_limits():
    _d.redis_conn.flushdb()
    logger.info('CORE address limits reset')


# object functions


def db_list(*args, **kwargs):
    return [dict(row) for row in get_db().execute(*args, **kwargs).fetchall()]


def delete_everything():
    get_db().execute(sql("""
            DELETE FROM addr
            """))


def addr_get(addr_id=None, addr=None):
    result = get_db().execute(sql(
        """SELECT id, a, active{} FROM addr WHERE id=:id or a=:a""".format(
            ',lim_c,lim_s' if _d.limits else '')),
                              id=addr_id,
                              a=addr).fetchone()
    if result:
        return dict(result)
    else:
        raise LookupError


def addr_list():
    return db_list(
        sql("""SELECT id, a, active{} FROM addr ORDER BY id""".format(
            ',lim_c, lim_s' if _d.limits else '')))


def addr_create():
    addr = gen_random_str(64)
    result = get_db().execute(sql("""
            INSERT INTO addr (a) VALUES (:a) {}
            """.format('' if is_use_lastrowid() else 'RETURNING id')),
                              a=addr)
    i = result.lastrowid if is_use_lastrowid() else result.fetchone().id
    return i


def addr_change(addr_id=None, addr=None, to=None):
    if to is None:
        to = gen_random_str(64)
    try:
        if get_db().execute(sql("""
                UPDATE addr SET a=:new_a WHERE id=:id or a=:a
                """),
                            new_a=to,
                            id=addr_id,
                            a=addr).rowcount:
            return to
    except sqlalchemy.exc.IntegrityError:
        raise ValueError
    else:
        raise LookupError


def addr_set_active(addr_id=None, addr=None, active=1):
    if get_db().execute(sql("""
            UPDATE addr SET active=:active WHERE id=:id or a=:a
            """),
                        active=active,
                        id=addr_id,
                        a=addr).rowcount:
        return addr_get(addr_id=addr_id, addr=addr)
    else:
        raise LookupError


def addr_set_limit(addr_id=None, addr=None, lim_c=None, lim_s=None):
    if lim_c is not None:
        if not get_db().execute(sql("""
                UPDATE addr SET lim_c=:lim_c WHERE id=:id or a=:a
                """),
                                lim_c=lim_c,
                                id=addr_id,
                                a=addr).rowcount:
            raise LookupError
    if lim_s is not None:
        if not get_db().execute(sql("""
                UPDATE addr SET lim_s=:lim_s WHERE id=:id or a=:a
                """),
                                lim_s=lim_s,
                                id=addr_id,
                                a=addr).rowcount:
            raise LookupError
    return addr_get(addr_id=addr_id, addr=addr)


def addr_delete(addr_id=None, addr=None):
    if not get_db().execute(sql("""
            DELETE FROM addr WHERE id=:id or a=:a
            """),
                            id=addr_id,
                            a=addr).rowcount:
        raise LookupError


def endpoint_get(endpoint_id):
    result = get_db().execute(
        sql("""SELECT id, addr_id, plugin_name, config, active,
                description FROM endpoint WHERE id=:id"""),
        id=endpoint_id).fetchone()
    if result:
        result = dict(result)
        if is_parse_db_json():
            result['config'] = json.loads(result['config'])
        return result
    else:
        raise LookupError


def endpoint_list(addr_id=None, addr=None):
    result = db_list(sql("""SELECT endpoint.id as id, addr_id, plugin_name,
        config, endpoint.active as active,
        description FROM endpoint JOIN addr ON addr.id=endpoint.addr_id
        WHERE addr.id=:addr_id OR addr.a=:addr ORDER BY id"""),
                     addr_id=addr_id,
                     addr=addr)
    if is_parse_db_json():
        for r in result:
            r['config'] = json.loads(r['config'])
    return result


def endpoint_create(plugin_name,
                    addr_id=None,
                    addr=None,
                    config=None,
                    description=None,
                    validate_config=False):
    if plugin_name not in plugins:
        raise LookupError(f'No such plugin: {plugin_name}')
    if config is None: config = {}
    else:
        try:
            safe_run_method(plugins[plugin_name], 'validate_config', config)
        except Exception as e:
            raise ValueError(e)
    result = get_db().execute(sql("""
            INSERT INTO endpoint (addr_id, plugin_name, config, description)
            VALUES (
                (SELECT id FROM addr where id=:addr_id or a=:addr),
                :plugin,
                :config,
                :description
            ) {}
            """.format('' if is_use_lastrowid() else 'RETURNING id')),
                              addr_id=addr_id,
                              addr=addr,
                              plugin=plugin_name,
                              config=json.dumps(config),
                              description=description)
    i = result.lastrowid if is_use_lastrowid() else result.fetchone().id
    logger.debug(f'CORE created endpoint {i} (plugin: {plugin_name})')
    return i


def endpoint_update(endpoint_id, data, validate_config=False, plugin_name=None):
    db = get_db()
    dbt = db.begin()
    try:
        if 'config' in data:
            try:
                if plugin_name is None:
                    plugin_name = endpoint_get(endpoint_id)['plugin_name']
                plugin = plugins[plugin_name]
            except KeyError:
                raise ValueError(f'plugin {plugin_name} not found')
            try:
                safe_run_method(plugin, 'validate_config', data['config'])
            except Exception as e:
                raise ValueError(e)
        for k, v in data.items():
            if k == 'active':
                v = int(v)
            if not db.execute(
                    sql(f"""
            UPDATE endpoint SET {k}=:v WHERE id=:id
            """),
                    id=endpoint_id,
                    v=json.dumps(v) if isinstance(v, dict) else v).rowcount:
                raise LookupError
        dbt.commit()
    except:
        dbt.rollback()
        raise


def endpoint_delete(endpoint_id):
    if not get_db().execute(
            sql("""
            DELETE FROM endpoint WHERE id=:id
            """),
            id=endpoint_id,
    ).rowcount:
        raise LookupError


def endpoint_delete_subscriptions(endpoint_id):
    return get_db().execute(
        sql("""
            DELETE FROM subscription WHERE endpoint_id=:id
            """),
        id=endpoint_id,
    ).rowcount


def subscription_get(subscription_id, endpoint_id=None):
    xkw = {'subscription_id': subscription_id}
    if endpoint_id is not None:
        xkw['endpoint_id'] = endpoint_id
    result = get_db().execute(
        sql("""SELECT
        subscription.id as id, addr.id as addr_id,
        endpoint_id, subscription.active as active, location, tag, sender,
        level, level_match
        FROM subscription
            JOIN endpoint ON endpoint.id=subscription.endpoint_id
            JOIN addr ON addr.id=endpoint.addr_id
        WHERE subscription.id=:subscription_id {}""".format(
            'AND endpoint_id=:endpoint_id' if endpoint_id is not None else '')),
        **xkw).fetchone()
    if result:
        return dict(result)
    else:
        raise LookupError


def subscription_list(endpoint_id, addr_id=None):
    xkw = {'endpoint_id': endpoint_id}
    if addr_id is not None:
        xkw['addr_id'] = addr_id
    return db_list(
        sql("""
        SELECT subscription.id as id, addr.id as addr_id,
            endpoint_id, subscription.active as active, location, tag,
            sender, level, level_match
        FROM subscription
            JOIN endpoint ON endpoint.id=subscription.endpoint_id
            JOIN addr ON addr.id=endpoint.addr_id
        WHERE endpoint.id=:endpoint_id {}
        ORDER BY id""".format(
            'AND addr.id=:addr_id' if addr_id is not None else '')), **xkw)


def subscription_create(endpoint_id,
                        location=None,
                        tag=None,
                        sender=None,
                        level=20,
                        level_match='ge'):
    if location == '': location = None
    if tag == '': tag = None
    if sender == '': sender = None
    if level is None: level = 20
    if level_match is None: level_match = 'ge'
    result = get_db().execute(sql("""
            INSERT INTO subscription (endpoint_id, location, tag,
                    sender, level, level_match)
            VALUES (
                :endpoint_id,
                :location,
                :tag,
                :sender,
                :level,
                :level_match
            ) {}
            """.format('' if is_use_lastrowid() else 'RETURNING id')),
                              endpoint_id=endpoint_id,
                              location=location,
                              tag=tag,
                              sender=sender,
                              level=level,
                              level_match=level_match)
    i = result.lastrowid if is_use_lastrowid() else result.fetchone().id
    logger.debug(f'CORE created subscription {i} for endpoint {endpoint_id}')
    return i


def subscription_update(subscription_id, data):
    db = get_db()
    dbt = db.begin()
    try:
        for k, v in data.items():
            if v == '' and k in ['location', 'tag', 'sender']:
                v = None
            elif k == 'level_match':
                if not v:
                    v = 'ge'
                elif v.endswith('t'):
                    v = v[0]
            elif k == 'active':
                v = int(v)
            if not db.execute(
                    sql(f"""
            UPDATE subscription SET {k}=:v WHERE id=:id
            """),
                    id=subscription_id,
                    v=json.dumps(v) if isinstance(v, dict) else v).rowcount:
                raise LookupError
        dbt.commit()
    except:
        dbt.rollback()
        raise


def subscription_delete(subscription_id):
    if not get_db().execute(
            sql("""
            DELETE FROM subscription WHERE id=:id
            """),
            id=subscription_id,
    ).rowcount:
        raise LookupError
