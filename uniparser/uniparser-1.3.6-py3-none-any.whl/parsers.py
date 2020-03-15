# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from hashlib import md5 as _md5
from itertools import chain
from logging import getLogger
from re import compile as re_compile
from string import Template
from time import localtime, mktime, strftime, strptime, timezone
from typing import Any, Dict, List, Union
from warnings import warn

from frequency_controller import AsyncFrequency, Frequency

from .config import GlobalConfig
from .exceptions import InvalidSchemaError
from .utils import (AsyncRequestAdapter, LazyImporter, SyncRequestAdapter,
                    ensure_request, get_available_async_request,
                    get_available_sync_request, get_host)

__all__ = [
    'BaseParser', 'ParseRule', 'CrawlerRule', 'HostRule', 'CSSParser',
    'XMLParser', 'RegexParser', 'JSONPathParser', 'ObjectPathParser',
    'JMESPathParser', 'PythonParser', 'UDFParser', 'LoaderParser', 'Uniparser'
]

logger = getLogger('uniparser')
lib = LazyImporter()
lib.register('from jmespath import compile as jmespath_compile',
             'jmespath_compile')
lib.register('from jsonpath_rw_ext import parse as jp_parse', 'jp_parse')
lib.register('from toml import loads as toml_loads', 'toml_loads')
lib.register('from bs4 import BeautifulSoup, Tag', ('BeautifulSoup', 'Tag'))
lib.register('from objectpath import Tree as OP_Tree', 'OP_Tree')
lib.register('from objectpath.core import ITER_TYPES', 'ITER_TYPES')
lib.register('from yaml import full_load as yaml_full_load', 'yaml_full_load')
lib.register('from yaml import safe_load as yaml_safe_load', 'yaml_safe_load')


def return_self(self, *args, **kwargs):
    return self


def md5(string, n=32, encoding="utf-8", skip_encode=False):
    """str(obj) -> md5_string

    :param string: string to operate.
    :param n: md5_str length.

    >>> md5(1, 10)
    '923820dcc5'
    >>> md5('test')
    '098f6bcd4621d373cade4e832627b4f6'
    """
    todo = string if skip_encode else str(string).encode(encoding)
    if n == 32:
        return _md5(todo).hexdigest()
    elif isinstance(n, (int, float)):
        return _md5(todo).hexdigest()[(32 - n) // 2:(n - 32) // 2]
    elif isinstance(n, (tuple, list)):
        return _md5(todo).hexdigest()[n[0]:n[1]]


class BaseParser(ABC):
    """Sub class of BaseParser should have these features:
    Since most input object always should be string, _RECURSION_LIST will be True.

    1. class variable `name`
    2. `_parse` method
    3. use lazy import, maybe
    4. Parsers will recursion parse list of input_object if it can only parse `str` object.

    Test demo::

        def _partial_test_parser():
            from uniparser import Uniparser

            uni = Uniparser()
            args = [
                ['adcb', 'sort', ''],
            ]
            max_len = max([len(str(i)) for i in args])
            for i in args:
                print(f'{str(i):<{max_len}} => {uni.python.parse(*i)}')


    """
    test_url = 'https://github.com/ClericPy/uniparser'
    doc_url = 'https://github.com/ClericPy/uniparser'
    name = 'base'
    _RECURSION_LIST = True
    __slots__ = ()

    @abstractmethod
    def _parse(self, input_object, param, value):
        pass

    def parse(self, input_object, param, value):
        try:
            if isinstance(input_object, list) and self._RECURSION_LIST:
                return [
                    self._parse(item, param, value) for item in input_object
                ]
            else:
                return self._parse(input_object, param, value)
        except Exception as err:
            # for traceback
            # import traceback; traceback.print_exc()
            return err


class CSSParser(BaseParser):
    """CSS selector parser, requires `bs4` and `lxml`(optional).
    Since HTML input object always should be string, _RECURSION_LIST will be True.

    Parse the input object with standard css selector, features from `BeautifulSoup`.

        :param input_object: input object, could be Tag or str.
        :type input_object: [Tag, str]
        :param param: css selector path
        :type param: [str]
        :param value: operation for each item of result
        :type value: [str]

            @attribute: return element.get(xxx)

            $text: return element.text

            $innerHTML, $html: return element.decode_contents()

            $outerHTML, $string: return str(element)

            $self: return element

        :return: list of Tag / str
        :rtype: List[Union[str, Tag]]

        examples:

            ['<a class="url" href="/">title</a>', 'a.url', '@href']      => ['/']
            ['<a class="url" href="/">title</a>', 'a.url', '$text']      => ['title']
            ['<a class="url" href="/">title</a>', 'a.url', '$innerHTML'] => ['title']
            ['<a class="url" href="/">title</a>', 'a.url', '$html']      => ['title']
            ['<a class="url" href="/">title</a>', 'a.url', '$outerHTML'] => ['<a class="url" href="/">title</a>']
            ['<a class="url" href="/">title</a>', 'a.url', '$string']    => ['<a class="url" href="/">title</a>']
            ['<a class="url" href="/">title</a>', 'a.url', '$self']      => [<a class="url" href="/">title</a>]

            WARNING: $self returns the original Tag object
    """
    name = 'css'
    doc_url = 'https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors'
    operations = {
        '@attr': lambda element: element.get(),
        '$text': lambda element: element.text,
        '$innerHTML': lambda element: element.decode_contents(),
        '$html': lambda element: element.decode_contents(),
        '$outerHTML': lambda element: str(element),
        '$string': lambda element: str(element),
        '$self': return_self,
    }

    def _parse(self, input_object, param, value):
        result = []
        if not input_object:
            return result
        # ensure input_object is instance of BeautifulSoup
        if not isinstance(input_object, lib.Tag):
            input_object = lib.BeautifulSoup(input_object, 'lxml')
        operate = self.operations.get(value, return_self)
        if value.startswith('@'):
            result = [
                item.get(value[1:], '') for item in input_object.select(param)
            ]
        else:
            result = [operate(item) for item in input_object.select(param)]
        return result


class XMLParser(BaseParser):
    """XML parser, requires `bs4` and `lxml`(necessary), but not support `xpath` for now.
    Since XML input object always should be string, _RECURSION_LIST will be True.

    Parse the input object with css selector, `BeautifulSoup` with features='xml'.

        :param input_object: input object, could be Tag or str.
        :type input_object: [Tag, str]
        :param param: css selector path
        :type param: [str]
        :param value: operation for each item of result
        :type value: [str]

            @attribute: return element.get(xxx)

            $text: return element.text

            $innerXML: return element.decode_contents()

            $outerXML: return str(element)

            $self: return element

        :return: list of Tag / str
        :rtype: List[Union[str, Tag]]

        examples:

            ['<dc:creator><![CDATA[author]]></dc:creator>', 'creator', '$text']      => ['author']
            WARNING: $self returns the original Tag object
    """
    name = 'xml'
    doc_url = 'https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors'
    operations = {
        '@attr': lambda element: element.get(),
        '$text': lambda element: element.text,
        '$innerXML': lambda element: element.decode_contents(),
        '$outerXML': lambda element: str(element),
        '$self': return_self,
    }

    def _parse(self, input_object, param, value):
        result = []
        if not input_object:
            return result
        # ensure input_object is instance of BeautifulSoup
        if not isinstance(input_object, lib.Tag):
            input_object = lib.BeautifulSoup(input_object, 'lxml-xml')
        operate = self.operations.get(value, return_self)
        if value.startswith('@'):
            result = [
                item.get(value[1:], '') for item in input_object.select(param)
            ]
        else:
            result = [operate(item) for item in input_object.select(param)]
        return result


class RegexParser(BaseParser):
    """RegexParser. Parse the input object with standard regex, features from `re`.
    Since regex input object always should be string, _RECURSION_LIST will be True.

        :param input_object: input object, could be str.
        :type input_object: [str]
        :param param: standard regex
        :type param: [str]
        :param value: operation for each item of result
        :type value: [str]

            @some string: using re.sub

            $0: re.finditer and return list of the whole matched string

            $1: re.finditer, $1 means return list of group 1

            '': null str, means using re.findall method

            -: return re.split(param, input_object)

        :return: list of str
        :rtype: List[Union[str]]

        examples:

            ['a a b b c c', 'a|c', '@b']     => 'b b b b b b'
            ['a a b b c c', 'a', '']         => ['a', 'a']
            ['a a b b c c', 'a (a b)', '$0'] => ['a a b']
            ['a a b b c c', 'a (a b)', '$1'] => ['a b']
            ['a a b b c c', 'b', '-']        => ['a a ', ' ', ' c c']
    """
    name = 're'
    test_url = 'https://regex101.com/'
    doc_url = 'https://docs.microsoft.com/en-us/dotnet/standard/base-types/regular-expression-language-quick-reference'
    VALID_VALUE_PATTERN = re_compile(r'^@|^\$\d+|^-$')

    def _parse(self, input_object, param, value):
        assert isinstance(input_object,
                          str), ValueError(r'input_object type should be str')
        assert self.VALID_VALUE_PATTERN.match(value) or not value, ValueError(
            r'args1 should match ^@|^\$\d+')
        com = re_compile(param)
        if not value:
            return com.findall(input_object)
        prefix, arg = value[0], value[1:]
        if prefix == '@':
            return com.sub(arg, input_object)
        elif prefix == '$':
            result = com.finditer(input_object)
            return [match.group(int(arg)) for match in result]
        elif prefix == '-':
            return com.split(input_object)


class JSONPathParser(BaseParser):
    """JSONPath parser, requires `jsonpath-rw-ext` lib.
    Since json input object may be dict / list, _RECURSION_LIST will be False.

        :param input_object: input object, could be str, list, dict.
        :type input_object: [str, list, dict]
        :param param: JSON path
        :type param: [str]
        :param value: attribute of find result, default to '' as '$value'
        :type value: [str, None]
        :return: list of str
        :rtype: List[Union[str]]

        examples:

            [{'a': {'b': {'c': 1}}}, '$..c', ''] => [1]
    """
    name = 'jsonpath'
    doc_url = 'https://github.com/sileht/python-jsonpath-rw-ext'
    test_url = 'https://jsonpath.com/'
    _RECURSION_LIST = False

    def _parse(self, input_object, param, value=''):
        if isinstance(input_object, str):
            input_object = GlobalConfig.json_loads(input_object)
        value = value or '$value'
        attr_name = value[1:]
        if param.startswith('JSON.'):
            param = '$%s' % param[4:]
        # try get the compiled jsonpath
        jsonpath_expr = getattr(param, 'code', lib.jp_parse(param))
        result = [
            getattr(match, attr_name, match.value)
            for match in jsonpath_expr.find(input_object)
        ]
        return result


class ObjectPathParser(BaseParser):
    """ObjectPath parser, requires `objectpath` lib.
    Since json input object may be dict / list, _RECURSION_LIST will be False.

        :param input_object: input object, could be str, list, dict.
        :type input_object: [str, list, dict]
        :param param: ObjectPath
        :type param: [str]
        :param value: not to use
        :type value: [Any]

        examples:

            [{'a': {'b': {'c': 1}}}, '$..c', ''] => [1]
    """
    name = 'objectpath'
    doc_url = 'http://github.com/adriank/ObjectPath'
    test_url = 'http://objectpath.org/'
    _RECURSION_LIST = False
    ITER_TYPES_TUPLE = tuple(lib.ITER_TYPES)

    def _parse(self, input_object, param, value=''):
        if isinstance(input_object, str):
            input_object = GlobalConfig.json_loads(input_object)
        if param.startswith('JSON.'):
            param = '$%s' % param[4:]
        tree = lib.OP_Tree(input_object)
        result = tree.execute(param)
        # from objectpath.core import ITER_TYPES
        if isinstance(result, self.ITER_TYPES_TUPLE):
            result = list(result)
        return result


class JMESPathParser(BaseParser):
    """JMESPath parser, requires `jmespath` lib.
    Since json input object may be dict / list, _RECURSION_LIST will be False.

        :param input_object: input object, could be str, list, dict.
        :type input_object: [str, list, dict]
        :param param: JMESPath
        :type param: [str]
        :param value: not to use
        :type value: [Any]

        examples:

            [{'a': {'b': {'c': 1}}}, 'a.b.c', ''] => 1
    """
    name = 'jmespath'
    doc_url = 'https://github.com/jmespath/jmespath.py'
    test_url = 'http://jmespath.org/'
    _RECURSION_LIST = False

    def _parse(self, input_object, param, value=''):
        if isinstance(input_object, str):
            input_object = GlobalConfig.json_loads(input_object)
        code = getattr(param, 'code', lib.jmespath_compile(param))
        return code.search(input_object)


class UDFParser(BaseParser):
    """UDFParser. Python source code snippets. globals will contain `input_object` and `context` variables.
    Since python input object may be any type, _RECURSION_LIST will be False.

        param & value:
            param: the python source code to be exec(param), either have the function named `parse`, or will return eval(param)
            value: will be renamed to `context`, which can be used in parser function. `value` often be set as the dict of request & response.
        examples:

            ['a b c d', 'input_object[::-1]', '']                                                       => 'd c b a'
            ['a b c d', 'context["key"]', {'key': 'value'}]                                             => 'value'
            ['a b c d', 'md5(input_object)', '']                                                        => '713f592bd537f7725d491a03e837d64a'
            ['["string"]', 'json_loads(input_object)', '']                                              => ['string']
            [['string'], 'json_dumps(input_object)', '']                                                => '["string"]'
            ['a b c d', 'parse = lambda input_object: input_object', '']                                => 'a b c d'
            ['a b c d', 'def parse(input_object): context["key"]="new";return context', {'key': 'old'}] => {'key': 'new'}
    """
    name = 'udf'
    doc_url = 'https://docs.python.org/3/'
    # can not import other libs
    _ALLOW_IMPORT = False
    # strict protection
    _ALLOW_EXEC_EVAL = False
    # Differ from others, treate list as list object
    _RECURSION_LIST = False
    # for udf globals, here could save some module can be used, such as: _GLOBALS_ARGS = {'requests': requests}
    _GLOBALS_ARGS = {
        'md5': md5,
        'json_loads': GlobalConfig.json_loads,
        'json_dumps': GlobalConfig.json_dumps,
    }

    @staticmethod
    def get_code_mode(code):
        if isinstance(code, CompiledString):
            return code.operator
        if 'parse' in code and ('lambda' in code or 'def ' in code):
            return exec
        else:
            return eval

    def _parse(self, input_object, param, value=""):
        # context could be any type, if string, will try to json.loads
        # if value is null, will use the context dict from CrawlerRule & ParseRule
        if value and isinstance(value, str):
            try:
                context = GlobalConfig.json_loads(value)
            except GlobalConfig.JSONDecodeError:
                context = {}
        else:
            context = value or {}
        if not self._ALLOW_IMPORT and 'import' in param:
            raise RuntimeError(
                'UDFParser._ALLOW_IMPORT is False, so source code should not has `import` strictly. If you really want it, set `UDFParser._ALLOW_IMPORT = True` manually'
            )
        if not self._ALLOW_EXEC_EVAL and 'exec' in param or 'eval' in param:
            raise RuntimeError(
                'UDFParser._ALLOW_EXEC_EVAL is False, so source code should not has `exec` `eval` strictly. If you really want it, set `UDFParser._ALLOW_EXEC_EVAL = True` manually'
            )
        # obj is an alias for input_object
        local_vars = {
            'input_object': input_object,
            'context': context,
            'obj': input_object
        }
        local_vars.update(self._GLOBALS_ARGS)
        # run code
        code = getattr(param, 'code', param)
        if self.get_code_mode(param) is exec:
            exec(code, local_vars, local_vars)
            parse_function = local_vars.get('parse')
            if not parse_function:
                raise ValueError(
                    'UDF snippet should have a function named `parse`')
            return parse_function(input_object)
        else:
            return eval(code, local_vars, local_vars)


class PythonParser(BaseParser):
    r"""PythonParser. Some frequently-used utils.
    Since python input object may be any type, _RECURSION_LIST will be False.

        :param input_object: input object, any object.
        :type input_object: [object]
        param & value:

            1.  param: getitem, alias to get
                value: could be [0] as index, [1:3] as slice, ['key'] for dict
            2.  param: split
                value: return input_object.split(value or None)
            3.  param: join
                value: return value.join(input_object)
            4.  param: chain
                value: nonsense `value` variable. return list(itertools.chain(*input_object))
            5.  param: const
                value: return value if value else input_object
            6.  param: template
                value: Template.safe_substitute(input_object=input_object, **input_object if isinstance(input_object, dict))
            7.  param: index
                value: value can be number string / key.
            8.  param: sort
                value: value can be asc (default) / desc.
            9.  param: strip
                value: chars. return str(input_object).strip(value)
        examples:

            [[1, 2, 3], 'getitem', '[-1]']              => 3
            [[1, 2, 3], 'getitem', '[:2]']              => [1, 2]
            [{'a': '1'}, 'getitem', 'a']                => '1'
            ['a b\tc \n \td', 'split', '']              => ['a', 'b', 'c', 'd']
            [['a', 'b', 'c', 'd'], 'join', '']          => 'abcd'
            [['aaa', ['b'], ['c', 'd']], 'chain', '']   => ['a', 'a', 'a', 'b', 'c', 'd']
            ['python', 'template', '1 $input_object 2'] => '1 python 2'
            [[1], 'index', '0']                         => 1
            ['python', 'index', '-1']                   => 'n'
            [{'a': '1'}, 'index', 'a']                  => '1'
            ['adcb', 'sort', '']                        => ['a', 'b', 'c', 'd']
            [[1, 3, 2, 4], 'sort', 'desc']              => [4, 3, 2, 1]
            ['aabbcc', 'strip', 'a']                    => 'bbcc'
            ['aabbcc', 'strip', 'ac']                   => 'bb'
            [' \t a ', 'strip', '']                     => 'a'
"""
    name = 'python'
    doc_url = 'https://docs.python.org/3/'
    # Differ from others, treate list as list object
    _RECURSION_LIST = False

    def _parse(self, input_object, param, value):
        param_functions = {
            'getitem': self._handle_getitem,
            'get': self._handle_getitem,
            'split': lambda input_object, param, value: input_object.split(value or None),
            'join': lambda input_object, param, value: value.join(input_object),
            'chain': lambda input_object, param, value: list(chain(*input_object)),
            'const': lambda input_object, param, value: value if value else input_object,
            'template': self._handle_template,
            'index': lambda input_object, param, value: input_object[int(value) if (value.isdigit() or value.startswith('-') and value[1:].isdigit()) else value],
            'sort': lambda input_object, param, value: sorted(input_object, reverse=(True if value.lower() == 'desc' else False)),
            'strip': self._handle_strip,
        }
        function = param_functions.get(param, return_self)
        return function(input_object, param, value)

    def _handle_strip(self, input_object, param, value):
        return str(input_object).strip(value or None)

    def _handle_template(self, input_object, param, value):
        if isinstance(input_object, dict):
            return Template(value).safe_substitute(
                input_object=input_object, **input_object)
        else:
            return Template(value).safe_substitute(input_object=input_object)

    def _handle_getitem(self, input_object, param, value):
        if value and (value[0], value[-1]) == ('[', ']'):
            value = value[1:-1]
            if ':' in value:
                # as slice
                start, stop = value.split(':', 1)
                if ':' in stop:
                    stop, step = stop.split(':')
                else:
                    step = None
                start = int(start) if start else None
                stop = int(stop) if stop else None
                step = int(step) if step else None
                key = slice(start, stop, step)
            else:
                # as index
                key = int(value)
            return input_object[key]
        else:
            return input_object[value]


class LoaderParser(BaseParser):
    """LoaderParser. Loads string with json / yaml / toml standard format.
    Since input object should be string, _RECURSION_LIST will be True.

        :param input_object: str match format of json / yaml / toml
        :type input_object: [str]
        :param param: loader name, such as: json, yaml, toml
        :type param: [str]
        :param value: some kwargs, input as json string
        :type value: [str]

        examples:

            ['{"a": "b"}', 'json', '']   => {'a': 'b'}
            ['a = "a"', 'toml', '']      => {'a': 'a'}
            ['animal: pets', 'yaml', ''] => {'animal': 'pets'}

    """
    name = 'loader'
    _RECURSION_LIST = True

    def __init__(self):
        self.loaders = {
            'json': GlobalConfig.json_loads,
            'toml': lib.toml_loads,
            'yaml': lib.yaml_full_load,
            'yaml_safe_load': lib.yaml_safe_load,
            'yaml_full_load': lib.yaml_full_load,
        }
        super().__init__()

    def _parse(self, input_object, param, value=''):
        loader = self.loaders.get(param, return_self)
        if value:
            try:
                kwargs = GlobalConfig.json_loads(value)
                return loader(input_object, **kwargs)
            except GlobalConfig.JSONDecodeError as err:
                return err
        else:
            return loader(input_object)


class TimeParser(BaseParser):
    """TimeParser. Parse different format of time. Sometimes time string need a preprocessing with regex.
    Since input object can not be list, _RECURSION_LIST will be True.
        To change time zone:
            uniparser.time.LOCAL_TIME_ZONE = +8

        :param input_object: str
        :type input_object: [str]
        :param param: encode / decode. encode: time string => timestamp; decode: timestamp => time string
        :type param: [str]
        :param value: standard strftime/strptime format
        :type value: [str]

        examples:

            ['2020-02-03 20:29:45', 'encode', '']                  => 1580732985.0
            ['1580732985.1873155', 'decode', '']                   => '2020-02-03 20:29:45'
            ['2020-02-03T20:29:45', 'encode', '%Y-%m-%dT%H:%M:%S'] => 1580732985.0
            ['1580732985.1873155', 'decode', '%b %d %Y %H:%M:%S']  => 'Feb 03 2020 20:29:45'

    WARNING: time.struct_time do not have timezone info, so %z is always the local timezone
    """
    name = 'time'
    match_int_float = re_compile(r'^-?\d+(\.\d+)?$')
    # EAST8 = +8, WEST8 = -8
    _OS_LOCAL_TIME_ZONE: int = -int(timezone / 3600)
    LOCAL_TIME_ZONE: int = _OS_LOCAL_TIME_ZONE

    def _parse(self, input_object, param, value):
        value = value or "%Y-%m-%d %H:%M:%S"
        tz_fix_seconds = (
            self.LOCAL_TIME_ZONE - self._OS_LOCAL_TIME_ZONE) * 3600
        if param == 'encode':
            # time string => timestamp
            if '%z' in value:
                msg = 'TimeParser Warning: time.struct_time do not have timezone info, so %z is nonsense'
                warn(msg)
                logger.warning(msg)
            return mktime(strptime(input_object, value)) - tz_fix_seconds
        elif param == 'decode':
            if isinstance(input_object,
                          str) and self.match_int_float.match(input_object):
                input_object = float(input_object)
            # timestamp => time string
            return strftime(value, localtime(input_object + tz_fix_seconds))
        else:
            return input_object


class CompiledString(str):
    __slots__ = ('operator', 'code')
    __support__ = ('jmespath', 'jsonpath', 'udf')

    def __new__(cls, string, mode=None, *args, **kwargs):
        if isinstance(string, cls):
            return string
        obj = str.__new__(cls, string, *args, **kwargs)
        obj = cls.compile(obj, string, mode)
        return obj

    @classmethod
    def compile(cls, obj, string, mode=None):
        if mode == 'jmespath':
            obj.code = lib.jmespath_compile(string)
        elif mode == 'jsonpath':
            obj.code = lib.jp_parse(string)
        elif mode == 'udf':
            obj.operator = UDFParser.get_code_mode(string)
            # for higher performance, pre-compile the code
            obj.code = compile(string, string, obj.operator.__name__)
        return obj


class JsonSerializable(dict):
    __slots__ = ()

    def __init__(self, **kwargs):
        super().__init__()
        self.update(kwargs)

    def to_dict(self):
        return dict(self)

    def dumps(self, *args, **kwargs):
        return GlobalConfig.json_dumps(self.to_dict(), *args, **kwargs)

    def to_json(self, *args, **kwargs):
        return self.dumps(*args, **kwargs)

    @classmethod
    def loads(cls, json_string):
        if isinstance(json_string, cls):
            return json_string
        return cls(**GlobalConfig.json_loads(json_string))

    @classmethod
    def from_json(cls, json_string):
        return cls.loads(json_string)


class ParseRule(JsonSerializable):
    """ParseRule should contain this params:
    1. a rule name, will be set as result key.
    2. chain_rules: a list of [[parser_name, param, value], ...], will be parse one by one.
    3. child_rules: a list of ParseRule instances, nested to save different values as named.
    4. context: a dict shared values by udf parse of the rules, only when udf value is null. May be shared from upstream CrawlerRule.

    Recursion parsing like a matryoshka doll.

    """
    __slots__ = ('context',)

    def __init__(self,
                 name: str,
                 chain_rules: List[List],
                 child_rules: List['ParseRule'] = None,
                 context: dict = None,
                 iter_parse_child: bool = False,
                 **kwargs):
        chain_rules = self.compile_codes(chain_rules or [])
        # ensure items of child_rules is ParseRule
        child_rules = [
            self.__class__(**parse_rule) for parse_rule in child_rules or []
        ]
        self.context: dict = context or {}
        super().__init__(
            name=name,
            chain_rules=chain_rules,
            child_rules=child_rules,
            **kwargs)
        if iter_parse_child:
            self['iter_parse_child'] = iter_parse_child

    @staticmethod
    def compile_rule(chain_rule):
        if isinstance(chain_rule[1], CompiledString):
            return chain_rule
        if chain_rule[0] in CompiledString.__support__:
            chain_rule[1] = CompiledString(chain_rule[1], mode=chain_rule[0])
        return chain_rule

    def compile_codes(self, chain_rules):
        return [self.compile_rule(chain_rule) for chain_rule in chain_rules]


class CrawlerRule(JsonSerializable):
    """A standard CrawlerRule contains:
    1. a rule name, will be set as result key.
    2. request_args for sending request.
    3. parse_rules: list of [ParseRule: , ...].
    4. regex: regex which can match a given url.
    5. context: a dict shared values by udf parse of the rules, only when udf value is null. May be shared to downstream ParseRule.
    6 **kwargs: some extra kwargs, sometimes contains encoding param.

    Rule format like:
        {
            "name": "crawler_rule",
            "request_args": {
                "method": "get",
                "url": "http://example.com",
                "headers": {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
                }
            },
            "parse_rules": [{
                "name": "parse_rule",
                "chain_rules": [["css", "p", "$text"], ["python", "getitem", "[0]"]],
                "child_rules": [{
                    "name": "rule1",
                    "chain_rules": [["python", "getitem", "[:7]"]],
                    "child_rules": [
                        {
                            "name": "rule2",
                            "chain_rules": [["udf", "input_object[::-1]", ""]],
                            "child_rules": []
                        },
                        {
                            "name": "rule3",
                            "chain_rules": [["udf", "input_object[::-1]", ""]],
                            "child_rules": [{
                                "name": "rule4",
                                "chain_rules": [["udf", "input_object[::-1]", ""]],
                                "child_rules": []
                            }]
                        }
                    ]
                }]
            }],
            "regex": ""
        }

    Parse Result like:
        {'crawler_rule': {'parse_rule': {'rule1': {'rule2': 'od sihT', 'rule3': {'rule4': 'This do'}}}}}
    """
    __slots__ = ('context',)
    CHECK_STRATEGY = 'match'

    def __init__(self,
                 name: str,
                 request_args: Union[dict, str],
                 parse_rules: List[ParseRule] = None,
                 regex: str = None,
                 context: dict = None,
                 **kwargs):
        _request_args: dict = ensure_request(request_args)
        if _request_args:
            _request_args["headers"] = _request_args.setdefault(
                "headers", {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
                })
        self.context = context or {}
        parse_rules = [
            ParseRule(context=self.context, **parse_rule)
            for parse_rule in parse_rules or []
        ]
        super().__init__(
            name=name,
            parse_rules=parse_rules,
            request_args=_request_args,
            regex=regex or '',
            **kwargs)

    def get_request(self, **request):
        if not request:
            return self['request_args']
        for k, v in self['request_args'].items():
            if k not in request:
                request[k] = v
        return request

    def add_parse_rule(self, rule: ParseRule, context: dict = None):
        rule = ParseRule(context=context or self.context, **rule)
        self['parse_rules'].append(rule)

    def pop_parse_rule(self, index, default=None):
        try:
            return self['parse_rules'].pop(index)
        except IndexError:
            return default

    def clear_parse_rules(self):
        self['parse_rules'].clear()

    def search(self, url):
        return not self['regex'] or re_compile(self['regex']).search(url)

    def match(self, url):
        return not self['regex'] or re_compile(self['regex']).match(url)

    def check_regex(self, url, strategy=''):
        return getattr(self, strategy or self.CHECK_STRATEGY)(url)


class HostRule(JsonSerializable):
    __slots__ = ()

    def __init__(self,
                 host: str,
                 crawler_rules: Dict[str, CrawlerRule] = None,
                 **kwargs):
        crawler_rules = {
            crawler_rule['name']: CrawlerRule(**crawler_rule)
            for crawler_rule in (crawler_rules or {}).values()
        }
        super().__init__(host=host, crawler_rules=crawler_rules, **kwargs)

    def find(self, url, strategy=''):
        rules = [
            rule for rule in self['crawler_rules'].values()
            if rule.check_regex(url, strategy)
        ]
        if len(rules) > 1:
            raise ValueError(f'{url} matched more than 1 rule. {rules}')
        if rules:
            return rules[0]

    def search(self, url):
        return self.find(url, 'search')

    def match(self, url):
        return self.find(url, 'match')

    def add_crawler_rule(self, rule: CrawlerRule):
        if not isinstance(rule, CrawlerRule) and isinstance(rule, str):
            rule = CrawlerRule.loads(rule)
        self['crawler_rules'][rule['name']] = rule
        try:
            assert get_host(rule['request_args']['url']) == self[
                'host'], f'different host: {self["host"]} not match {rule["request_args"]["url"]}'
            assert self.match(rule['request_args']['url']) or self.search(
                rule['request_args']['url']
            ), f'regex {rule["regex"]} not match the given url: {rule["request_args"]["url"]}'
        except (ValueError, KeyError, AssertionError) as e:
            self['crawler_rules'].pop(rule['name'], None)
            raise e

    def pop_crawler_rule(self, rule_name: str):
        return self['crawler_rules'].pop(rule_name, None)


class Uniparser(object):
    """Parsers collection.
    """
    _RECURSION_CRAWL = True
    _DEFAULT_FREQUENCY = Frequency()
    _DEFAULT_ASYNC_FREQUENCY = AsyncFrequency()
    _HOST_FREQUENCIES: Dict[str, Union[Frequency, AsyncFrequency]] = {}

    def __init__(self,
                 request_adapter: Union[AsyncRequestAdapter,
                                        SyncRequestAdapter] = None):
        self._prepare_default_parsers()
        self._prepare_custom_parsers()
        self.request_adapter = request_adapter

    def _prepare_default_parsers(self):
        self.css = CSSParser()
        self.xml = XMLParser()
        self.re = RegexParser()
        self.jsonpath = JSONPathParser()
        self.objectpath = ObjectPathParser()
        self.jmespath = JMESPathParser()
        self.python = PythonParser()
        self.udf = UDFParser()
        self.loader = LoaderParser()
        self.time = TimeParser()

    def _prepare_custom_parsers(self):
        # handle the other sublclasses
        for parser in BaseParser.__subclasses__():
            if parser.name not in self.__dict__:
                self.__dict__[parser.name] = parser()

    # for alias
    @property
    def py(self):
        return self.python

    @property
    def parser_classes(self):
        return BaseParser.__subclasses__()

    def parse_chain(self, input_object, chain_rules: List, context=None):
        for parser_name, param, value in chain_rules:
            parser = getattr(self, parser_name)
            if not parser:
                msg = f'Skip parsing for unknown name: {parser_name}'
                warn(msg)
                logger.warning(msg)
                continue
            if context and parser_name == 'udf' and not value:
                value = context
            input_object = parser.parse(input_object, param, value)
        return input_object

    def parse_crawler_rule(self, input_object, rule: CrawlerRule, context=None):
        parse_rules = rule['parse_rules']
        parse_result: Dict[str, Any] = {}
        context = context or rule.context
        for parse_rule in parse_rules:
            context['parse_result'] = parse_result
            parse_result[parse_rule['name']] = self.parse_parse_rule(
                input_object, parse_rule, context).get(parse_rule['name'])
        context.pop('parse_result', None)
        return {rule['name']: parse_result}

    def parse_parse_rule(self, input_object, rule: ParseRule, context=None):
        # if context, use context; else use rule.context
        input_object = self.parse_chain(
            input_object,
            rule['chain_rules'],
            context=context or getattr(rule, 'context', {}))
        if rule['name'] == GlobalConfig.__schema__ and input_object is not True:
            raise InvalidSchemaError(
                f'Schema check is not True: {input_object}')
        result = {rule['name']: input_object}
        if not rule['child_rules']:
            return {rule['name']: input_object}
        else:
            result = {rule['name']: {}}
        if rule.get('iter_parse_child', False):
            result[rule['name']] = []
            for partial_input_object in input_object:
                partial_result = {}
                for sub_rule in rule['child_rules']:
                    partial_result[sub_rule['name']] = self.parse_parse_rule(
                        partial_input_object,
                        sub_rule,
                        context=context,
                    ).get(sub_rule['name'])
                result[rule['name']].append(partial_result)
        else:
            for sub_rule in rule['child_rules']:
                result[rule['name']][sub_rule['name']] = self.parse_parse_rule(
                    input_object,
                    sub_rule,
                    context=context,
                ).get(sub_rule['name'])
        return result

    def parse(self,
              input_object,
              rule_object: Union[CrawlerRule, ParseRule],
              context=None):
        if isinstance(rule_object, CrawlerRule):
            return self.parse_crawler_rule(
                input_object=input_object, rule=rule_object, context=context)
        elif isinstance(rule_object, ParseRule):
            return self.parse_parse_rule(
                input_object=input_object, rule=rule_object, context=context)

    def ensure_adapter(self, sync=True):
        if self.request_adapter:
            request_adapter = self.request_adapter
            if sync and isinstance(request_adapter, SyncRequestAdapter) or (
                    not sync) and isinstance(request_adapter,
                                             AsyncRequestAdapter):
                return self.request_adapter
        if sync:
            self.request_adapter = get_available_sync_request()()
        else:
            self.request_adapter = get_available_async_request()()
        return self.request_adapter

    def download(self,
                 crawler_rule: CrawlerRule,
                 request_adapter=None,
                 **request):
        request_adapter = request_adapter or self.ensure_adapter(sync=True)
        if not isinstance(request_adapter, SyncRequestAdapter):
            raise RuntimeError('bad request_adapter type')
        request_args = crawler_rule.get_request(**request)
        host = get_host(request_args['url'])
        freq = self._HOST_FREQUENCIES.get(host, self._DEFAULT_FREQUENCY)
        with freq:
            with request_adapter as req:
                input_object, resp = req.request(**request_args)
        return input_object, resp

    def crawl(self,
              crawler_rule: CrawlerRule,
              request_adapter=None,
              context=None,
              **request):
        input_object, resp = self.download(crawler_rule, request_adapter,
                                           **request)
        if isinstance(resp, Exception):
            return resp
        context = context or crawler_rule.context
        for k, v in crawler_rule.context.items():
            if k not in context:
                context[k] = v
        context['resp'] = resp
        return self.parse(input_object, crawler_rule, context)

    async def adownload(self,
                        crawler_rule: CrawlerRule,
                        request_adapter=None,
                        **request):
        request_adapter = request_adapter or self.ensure_adapter(sync=False)
        if not isinstance(request_adapter, AsyncRequestAdapter):
            raise RuntimeError('bad request_adapter type')
        request_args = crawler_rule.get_request(**request)
        host = get_host(request_args['url'])
        freq = self._HOST_FREQUENCIES.get(host, self._DEFAULT_ASYNC_FREQUENCY)
        async with freq:
            async with request_adapter as req:
                input_object, resp = await req.request(**request_args)
        return input_object, resp

    async def acrawl(self,
                     crawler_rule: CrawlerRule,
                     request_adapter=None,
                     context=None,
                     **request):
        input_object, resp = await self.adownload(crawler_rule, request_adapter,
                                                  **request)
        if isinstance(resp, Exception):
            return resp
        context = context or crawler_rule.context
        for k, v in crawler_rule.context.items():
            if k not in context:
                context[k] = v
        context['resp'] = resp
        return self.parse(input_object, crawler_rule, context)

    @classmethod
    def set_frequency(cls, host_or_url: str, n=0, interval=0):
        host = get_host(host_or_url, host_or_url)
        cls._HOST_FREQUENCIES[host] = Frequency(n, interval)

    @classmethod
    def set_async_frequency(cls, host_or_url: str, n=0, interval=0):
        host = get_host(host_or_url, host_or_url)
        cls._HOST_FREQUENCIES[host] = AsyncFrequency(n, interval)

    @classmethod
    def pop_frequency(cls, host_or_url: str, default=None):
        host = get_host(host_or_url, host_or_url)
        return cls._HOST_FREQUENCIES.pop(host, default)
