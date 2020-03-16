# pylint: disable=django-not-available,invalid-name
from __future__ import unicode_literals

import collections
import json
import logging
import os
import io
import sys
import tempfile
import time
import traceback
import subprocess
from pathlib import Path
from threading import Thread
import typing as tp

from django.core.cache import caches, InvalidCacheBackendError
from django.core.paginator import Paginator as BasePaginator
from django.conf.urls import url, include
from django.template import loader
from django.utils import translation
from django.utils.module_loading import import_string as import_class
from django.views.decorators.csrf import csrf_exempt

from . import exceptions as ex

logger = logging.getLogger('vstutils')
ON_POSIX = 'posix' in sys.builtin_module_names


def get_render(name: tp.Text, data: tp.Dict, trans: tp.Text = 'en') -> tp.Text:
    """
    Render string from template.

    :param name: -- full template name
    :type name: str,unicode
    :param data: -- dict of rendered vars
    :type data: dict
    :param trans: -- translation for render. Default 'en'.
    :type trans: str,unicode
    :return: -- rendered string
    :rtype: str,unicode
    """
    translation.activate(trans)
    config = loader.get_template(name)
    result = config.render(data).replace('\r', '')
    translation.deactivate()
    return result


class ClassPropertyMeta(type):
    def __setattr__(cls, key, value):
        obj = cls.__dict__.get(key, None)
        if isinstance(obj, ClassPropertyDescriptor):
            return obj.__set__(cls, value)
        return super().__setattr__(key, value)


class ClassPropertyDescriptor:
    __slots__ = 'fget', 'fset'

    meta = ClassPropertyMeta

    def __init__(self, fget: tp.Callable, fset: tp.Callable = None):
        self.fget = self._fix_function(fget)
        self.fset = self._fix_function(fset)

    def __get__(self, obj, klass=None):
        if obj is not None:
            return self.fget.__get__(obj, obj)()
        return self.fget.__get__(obj, type(obj) if klass is None else klass)()

    def __set__(self, obj: tp.Any, value: tp.Any):
        if not self.fset:
            raise AttributeError("can't set attribute")
        if obj is not None:
            return self.fset.__get__(obj, obj)(value)
        return self.fset.__get__(obj, type(obj))(value)  # nocv

    def setter(self, func: tp.Callable):
        if not isinstance(func, (classmethod, staticmethod)):
            func = classmethod(func)
        self.fset = func
        return self

    @classmethod
    def _fix_function(cls, func):
        if func is None:
            return func
        if not isinstance(func, (classmethod, staticmethod)):
            func = classmethod(func)
        return func


class classproperty(ClassPropertyDescriptor):
    """
    Decorator which makes class method as class property.

    Example:
        .. sourcecode:: python

            from vstutils.utils import classproperty

            class SomeClass(metaclass=classproperty.meta):
                # Metaclass is needed for set attrs in class
                # instead of and not only object.

                some_value = None

                @classproperty
                def value(cls):
                    return cls.some_value

                @value.setter
                def value(cls, new_value):
                    cls.some_value = new_value
    """


class redirect_stdany:
    """
    Context for redirect any output to own stream.

    .. note::
        - On context return stream object.
        - On exit return old streams
    """
    __slots__ = 'stream', 'streams', '_old_streams'

    _streams = ["stdout", "stderr"]  # type: list

    def __init__(self, new_stream=io.StringIO(), streams=None):
        """
        :param new_stream: -- stream where redirects all
        :type new_stream: object
        :param streams: -- names of streams like ``['stdout', 'stderr']``
        :type streams: list
        """
        self.streams = streams or self._streams
        self.stream = new_stream
        self._old_streams = {}

    def __enter__(self):
        for stream in self.streams:
            self._old_streams[stream] = getattr(sys, stream)
            setattr(sys, stream, self.stream)
        return self.stream

    def __exit__(self, exctype, excinst, exctb):
        for stream in self.streams:
            setattr(sys, stream, self._old_streams.pop(stream))


class Dict(collections.OrderedDict):
    """
    Wrapper over `collections.OrderedDict` which
    return JSON on conversion to string.
    """

    def __repr__(self):  # nocv
        return self.__str__()

    def __str__(self):  # nocv
        return self.__unicode__()

    def __unicode__(self):  # nocv
        return json.dumps(self)


class tmp_file:
    """
    Temporary file with name
    generated and auto removed on close.
    """
    __slots__ = ('fd', 'path',)

    def __init__(self, data: tp.Text = "", mode: tp.Text = "w", bufsize: int = -1, **kwargs):
        """
        tmp_file constructor

        :param data: -- string to write in tmp file.
        :type data: str
        :param mode: -- file open mode. Default 'w'.
        :type mode: str
        :param bufsize: -- bufer size for tempfile.NamedTemporaryFile
        :type bufsize: int
        :param kwargs:  -- other kwargs for tempfile.NamedTemporaryFile
        """
        self.fd = tempfile.NamedTemporaryFile(mode, buffering=bufsize, **kwargs)
        self.path = Path(self.fd.name)
        if data:
            self.write(data)

    def write(self, wr_string: tp.Text):
        """
        Write to file and flush

        :param wr_string: -- writable string
        :type wr_string: str
        :return: None
        :rtype: None
        """
        result = self.fd.write(wr_string)
        self.fd.flush()
        return result

    def __getattr__(self, name: tp.Text):
        return getattr(self.fd, name)

    def __del__(self):
        with raise_context():
            self.fd.close()

    def __enter__(self):
        """
        :return: -- file object
        :rtype: tempfile.NamedTemporaryFile
        """
        return self

    def __exit__(self, type_e, value, tb):
        self.fd.close()
        if value is not None:
            return False


class tmp_file_context:
    """
    Context object for work with tmp_file.
    Auto close on exit from context and
    remove if file still exist.
    """
    __slots__ = ('tmp',)

    def __init__(self, *args, **kwargs):
        self.tmp = tmp_file(*args, **kwargs)  # type: tempfile.NamedTemporaryFile

    def __enter__(self):
        return self.tmp

    def __exit__(self, type_e, value, tb):
        self.tmp.close()
        if self.tmp.path.exists():
            self.tmp.path.unlink()


class assertRaises:

    def __init__(self, *args, **kwargs):
        """
        :param args: -- list of exception classes should be passed
        :type args: list,Exception
        :param exclude: -- list of exception classes should be raised
        :type exclude: list,Exception
        :param verbose: -- logging
        :type verbose: bool
        """
        self._kwargs = dict(**kwargs)
        self._verbose = kwargs.pop("verbose", False)
        self._exclude = kwargs.pop("exclude", False)
        self._excepts = tuple(args)

    def __enter__(self):
        return self  # pragma: no cover

    def __exit__(self, exc_type, exc_val, exc_tb):
        return exc_type is not None and (
                (not self._exclude and not issubclass(exc_type, self._excepts)) or
                (self._exclude and issubclass(exc_type, self._excepts))
        )


# noinspection PyUnreachableCode
class raise_context(assertRaises):
    """
    Context for exclude exceptions.
    """

    def execute(self, func: tp.Callable, *args, **kwargs):
        with self.__class__(self._excepts, **self._kwargs):
            return func(*args, **kwargs)
        type, value, traceback_obj = sys.exc_info()
        if type is not None:  # nocv
            logger.debug(traceback.format_exc())
        return type, value, traceback_obj

    def __enter__(self):
        return self.execute

    def __call__(self, original_function: tp.Callable):
        def wrapper(*args, **kwargs):
            return self.execute(original_function, *args, **kwargs)

        return wrapper


class exception_with_traceback(raise_context):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val is not None:
            exc_val.traceback = traceback.format_exc()
            # six.reraise(exc_type, exc_val, exc_tb)
            raise exc_val.with_traceback(exc_tb)


class BaseVstObject:
    """
    Default mixin-class for custom objects which needed to get settings and cache.
    """

    @classmethod
    def get_django_settings(cls, name: tp.Text, default: tp.Any = None):
        # pylint: disable=access-member-before-definition
        """
        Get params from Django settings.

        :param name: name of param
        :type name: str,unicode
        :param default: default value of param
        :type default: object
        :return: Param from Django settings or default.
        """
        if hasattr(cls, '__django_settings__'):
            return getattr(cls.__django_settings__, name, default)
        from django.conf import settings
        cls.__django_settings__ = settings
        return cls.get_django_settings(name)

    @classmethod
    def get_django_cache(cls, cache_name: tp.Text = 'default'):
        try:
            return caches[cache_name]
        except InvalidCacheBackendError:  # nocv
            return caches['default']


class Executor(BaseVstObject):
    """
    Command executor with realtime output write.
    """
    __slots__ = 'output', '_stdout', '_stderr', 'env'

    CANCEL_PREFIX = "CANCEL_EXECUTE_"  # type: str
    newlines = ['\n', '\r\n', '\r']  # type: list
    STDOUT = subprocess.PIPE
    STDERR = subprocess.STDOUT
    DEVNULL = subprocess.DEVNULL
    CalledProcessError = subprocess.CalledProcessError

    def __init__(self, stdout=subprocess.PIPE, stderr=subprocess.STDOUT):
        """

        :type stdout: BinaryIO,int
        :type stderr: BinaryIO,int
        """
        self.output = ''
        self._stdout = stdout
        self._stderr = stderr
        self.env = {}

    def write_output(self, line: tp.Text):
        """
        :param line: -- line from command output
        :type line: str
        :return: None
        :rtype: None
        """
        self.output += str(line)

    def _handle_process(self, proc: subprocess.Popen, stream: tp.Text):
        stream_object = getattr(proc, stream)
        while not stream_object.closed:
            self.working_handler(proc)
            time.sleep(0.1)

    def working_handler(self, proc: subprocess.Popen):
        # pylint: disable=unused-argument
        """
        Additional handler for executions.

        :type proc: subprocess.Popen
        """

    def _unbuffered(self, proc: subprocess.Popen, stream: tp.Text = 'stdout'):
        """
        Unbuffered output handler.

        :type proc: subprocess.Popen
        :type stream: str
        :return:
        """
        if self.working_handler is not None:
            t = Thread(target=self._handle_process, args=(proc, stream))
            t.start()
        out = getattr(proc, stream)
        try:
            retcode = None
            while retcode is None:
                for line in iter(out.readline, ""):
                    yield line.rstrip()
                retcode = proc.poll()
        finally:
            out.close()

    def line_handler(self, line: tp.Text):
        """
        Per line handler.

        :type line: str
        """
        if line is not None:
            with raise_context():
                self.write_output(line)

    def execute(self, cmd, cwd: tp.Union[tp.Text, Path]):
        """
        Execute commands and output this.

        :param cmd: -- list of cmd command and arguments
        :type cmd: list
        :param cwd: -- workdir for executions
        :type cwd: str
        :return: -- string with full output
        :rtype: str
        """
        self.output = ""
        env = os.environ.copy()
        env.update(self.env)
        proc = subprocess.Popen(
            cmd, stdout=self._stdout, stderr=self._stderr,
            bufsize=0, universal_newlines=True,
            cwd=str(cwd), env=env,
            close_fds=ON_POSIX
        )
        for line in self._unbuffered(proc):
            self.line_handler(line)
        return_code = proc.poll()
        if return_code:
            logger.error(self.output)
            raise subprocess.CalledProcessError(
                return_code, cmd, output=str(self.output)
            )
        return self.output


class UnhandledExecutor(Executor):
    working_handler = None


class KVExchanger(BaseVstObject):
    """
    Class for transmit data using key-value fast (cache-like) storage between
    services. Uses same cache-backend as Lock.
    """
    TIMEOUT = 60  # type: int

    @classproperty
    def PREFIX(cls):
        # pylint: disable=no-self-argument
        return f"{cls.get_django_settings('VST_PROJECT_LIB')}_exchange_"

    @classproperty
    def cache(cls):
        # pylint: disable=no-self-argument,no-member
        if hasattr(cls, '__django_cache__'):
            return getattr(cls, '__django_cache__')
        cls.__django_cache__ = cls.get_django_cache('locks')
        return cls.cache

    def __init__(self, key, timeout=None):
        self.key = self.PREFIX + str(key)
        self.timeout = timeout or self.TIMEOUT

    def send(self, value, ttl=None):
        # pylint: disable=no-member
        return self.cache.add(self.key, value, ttl or self.timeout)

    def prolong(self, ttl=None):
        # pylint: disable=no-member
        payload = self.cache.get(self.key)
        self.cache.set(self.key, payload, ttl or self.timeout)

    def get(self):
        # pylint: disable=no-member
        value = self.cache.get(self.key)
        self.cache.delete(self.key)
        return value

    def delete(self):
        # pylint: disable=no-member
        self.cache.delete(self.key)


class Lock(KVExchanger):
    """
    Lock class for multi-jobs workflow.

    .. note::
        - Used django.core.cache lib and settings in `settings.py`
        - Have Lock.SCHEDULER and Lock.GLOBAL id
    """
    TIMEOUT = 60 * 60 * 24  # type: int
    GLOBAL = "global-deploy"  # type: str
    SCHEDULER = "celery-beat"  # type: str

    class AcquireLockException(Exception):
        pass

    @classproperty
    def PREFIX(cls):
        # pylint: disable=no-self-argument
        return f"{cls.get_django_settings('VST_PROJECT_LIB')}_lock_"

    def __init__(self, id, payload=None, repeat=1, err_msg="", timeout=None):
        # pylint: disable=too-many-arguments
        """
        :param id: -- unique id for lock.
        :type id: int,str
        :param payload: -- lock additional info.
        :param repeat: -- time to wait lock.release. Default 1 sec.
        :type repeat: int
        :param err_msg: -- message for AcquireLockException error.
        :type err_msg: str
        """
        super().__init__(id, timeout)
        self.id, start = None, time.time()
        while time.time() - start <= repeat:
            if self.send(payload):
                self.id = id
                return
            time.sleep(0.01)
        raise self.AcquireLockException(err_msg)

    def get(self):  # nocv
        # pylint: disable=no-member
        return self.cache.get(self.key)

    def __enter__(self):
        return self

    def __exit__(self, type_e, value, tb):
        self.release()

    def release(self):
        # pylint: disable=no-member
        self.cache.delete(self.key)

    def __del__(self):
        self.release()


class __LockAbstractDecorator:
    _err = "Wait until the end."
    _lock_key = None

    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.kwargs["err_msg"] = self.kwargs.get("err_msg", self._err)

    def execute(self, func, *args, **kwargs):
        if self._lock_key is not None:
            with Lock(self._lock_key, **self.kwargs):
                return func(*args, **kwargs)
        return func(*args, **kwargs)

    def __call__(self, original_function):
        def wrapper(*args, **kwargs):
            return self.execute(original_function, *args, **kwargs)

        return wrapper


class model_lock_decorator(__LockAbstractDecorator):
    """
    Decorator for functions where 'pk' kwarg exist
    for lock by id.

    .. warning::
        - On locked error raised ``Lock.AcquireLockException``
        - Method must have and called with ``pk`` named arg.

    """
    _err = "Object locked. Wait until unlock."

    def execute(self, func, *args, **kwargs):
        self._lock_key = kwargs.get('pk', None)
        return super().execute(func, *args, **kwargs)


class Paginator(BasePaginator):
    """
    Class for fragmenting the query for small queries.
    """

    def __init__(self, qs, chunk_size=None):
        """
        :param qs: -- queryset for fragmenting
        :type qs: django.db.models.QuerySet
        :param chunk_size: -- size of the fragments.
        :type chunk_size: int
        """
        chunk_size = chunk_size or BaseVstObject().get_django_settings("PAGE_LIMIT", None)
        super().__init__(qs, chunk_size)

    def __iter__(self):
        for page in range(1, self.num_pages + 1):
            yield self.page(page)

    def items(self):
        for page in self:
            for obj in page.object_list:
                obj.paginator = self
                obj.page = page
                yield obj


class ObjectHandlers(BaseVstObject):
    """
    Handlers wrapper for get objects from some settings structure.

    Example:
        .. sourcecode:: python

            from vstutils.utils import ObjectHandlers

            '''
            In `settings.py` you should write some structure:

            SOME_HANDLERS = {
                "one": {
                    "BACKEND": "full.python.path.to.module.SomeClass"
                },
                "two": {
                    "BACKEND": "full.python.path.to.module.SomeAnotherClass",
                    "OPTIONS": {
                        "some_named_arg": "value"
                    }
                }
            }
            '''

            handlers = ObjectHandlers('SOME_HANDLERS')

            # Get class handler for 'one'
            one_backend_class = handlers['one']
            # Get object of backend 'two'
            two_obj = handlers.get_object()
            # Get object of backend 'two' with overriding constructor named arg
            two_obj_overrided = handlers.get_object(some_named_arg='another_value')

    """

    __slots__ = 'type', 'err_message', '_list', '_loaded_backends'

    def __init__(self, type_name: tp.Text, err_message: tp.Text = None):
        """
        :param type_name: -- type name for backends.Like name in dict.
        :type type_name: str
        """
        self.type = type_name  # type: tp.Text
        self.err_message = err_message  # type: tp.Optional[tp.Text]
        self._list = None  # type: tp.Optional[tp.Dict[tp.Text, tp.Any]]
        self._loaded_backends = dict()  # type: tp.Dict[tp.Text, tp.Any]

    @property
    def objects(self):
        return {name: self[name] for name in self.list()}

    def __len__(self):  # pragma: no cover
        return len(self.objects)

    def __iter__(self):
        return iter(self.items())

    def __getitem__(self, name):
        return self.backend(name)

    def __call__(self, name, obj):
        return self.get_object(name, obj)

    def __dict__(self):  # pragma: no cover
        return self.items()

    def keys(self) -> tp.Iterable[tp.Text]:
        return self.objects.keys()

    def values(self) -> tp.Iterable:  # pragma: no cover
        return dict(self).values()

    def items(self):
        return self.objects.items()

    def list(self) -> tp.Dict[tp.Text, tp.Dict[tp.Text, tp.Any]]:
        if self._list is None:
            self._list = self.get_django_settings(self.type, {})
        return self._list

    def _get_baskend(self, backend):
        if backend in self._loaded_backends:
            return self._loaded_backends[backend]
        self._loaded_backends[backend] = import_class(backend)
        return self._loaded_backends[backend]

    def get_backend_data(self, name: tp.Text):
        return self.list()[name]

    def get_backend_handler_path(self, name: tp.Text):
        return self.get_backend_data(name).get('BACKEND', None)

    def backend(self, name: tp.Text):
        """
        Get backend class

        :param name: -- name of backend type
        :type name: str
        :return: class of backend
        :rtype: class,module,object
        """
        try:
            backend = self.get_backend_handler_path(name)
            if backend is None:
                raise ex.VSTUtilsException("Backend is 'None'.")  # pragma: no cover
            return self._get_baskend(backend)
        except KeyError or ImportError:
            msg = f"{name} ({self.err_message})" if self.err_message else name
            raise ex.UnknownTypeException(msg)

    def opts(self, name: tp.Text):
        return self.get_backend_data(name).get('OPTIONS', {})

    def get_object(self, name: tp.Text, *args, **kwargs):
        opts = self.opts(name)
        opts.update(kwargs)
        return self[name](*args, **opts)


class ModelHandlers(ObjectHandlers):
    """
    Handlers for some models like 'INTEGRATIONS' or 'REPO_BACKENDS'.
    All handlers backends get by first argument model object.

    **Attributes**:

    :param objects: -- dict of objects like: ``{<name>: <backend_class>}``
    :type objects: dict
    :param keys: -- names of supported backends
    :type keys: list
    :param values: -- supported backends classes
    :type values: list
    """

    def get_object(self, name: tp.Text, obj):
        """
        :param name: -- string name of backend
        :param name: str
        :param obj: -- model object
        :type obj: django.db.models.Model
        :return: backend object
        :rtype: object
        """
        return self[name](obj, **self.opts(name))


class URLHandlers(ObjectHandlers):
    """ Object handler for GUI views. Uses `GUI_VIEWS` from settings.py. """
    __slots__ = ('additional_handlers', '__handlers__')

    settings_urls = ['LOGIN_URL', 'LOGOUT_URL']  # type: list

    def __init__(self, type_name: tp.Text = 'GUI_VIEWS', *args, **kwargs):
        self.additional_handlers = kwargs.pop('additional_handlers', ['VIEWS']) + [type_name]
        super().__init__(type_name, *args, **kwargs)

    @property
    def view_handlers(self):
        if not hasattr(self, '__handlers__'):
            self.__handlers__ = []
            handler_class = self.__class__
            for handler_settings_name in self.additional_handlers:
                self.__handlers__.append(handler_class(handler_settings_name))
        return self.__handlers__

    def get_backend_data(self, name: tp.Text):
        data = super().get_backend_data(name)
        if isinstance(data, str):
            for handler in self.view_handlers:
                try:
                    handler_data = handler.get_backend_data(data)
                except:
                    continue
                if handler_data:
                    return handler_data
        return data

    def get_object(self, name: tp.Text, *argv, **kwargs):
        """
        Get url object tuple for urls.py

        :param name: url regexp from
        :type name: str
        :param argv: overrided args
        :param kwargs: overrided kwargs
        :return: url object
        :rtype: django.conf.urls.url
        """
        regexp = name
        options = self.opts(regexp)
        options.update(kwargs)
        args = options.pop('view_args', argv)
        view_kwargs = options.pop('view_kwargs', {})
        csrf_enable = self.get_backend_data(regexp).get('CSRF_ENABLE', True)
        if regexp in self.settings_urls:
            regexp = rf'^{self.get_django_settings(regexp)[1:]}'
        view_class = self[name]
        if hasattr(view_class, 'as_view'):
            view = view_class.as_view(**view_kwargs)
            if not csrf_enable:
                view = csrf_exempt(view)
            result = url(regexp, view, *args, **options)
        else:
            result = url(regexp, include(view_class))
        return result

    def urls(self) -> tp.Iterable:
        for regexp in self.list():
            yield self.get_object(regexp)
