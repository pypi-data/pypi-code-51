"""
@file
@brief Overwrites unit test class with additional testing functions.
"""
from io import StringIO
import os
import sys
import unittest
import warnings
import decimal
from contextlib import redirect_stdout, redirect_stderr
from .ci_helper import is_travis_or_appveyor
from .profiling import profile
from ..texthelper import compare_module_version


class ExtTestCase(unittest.TestCase):
    """
    Overwrites unit test class with additional testing functions.
    Unless *setUp* is overwritten, warnings *FutureWarning* and
    *PendingDeprecationWarning* are filtered out.
    """

    def setUp(self):
        """
        Filters out *FutureWarning*, *PendingDeprecationWarning*.
        """
        warnings.simplefilter("ignore",
                              (FutureWarning,
                               PendingDeprecationWarning,
                               ImportWarning,
                               DeprecationWarning))

    def tearDown(self):
        """
        Stops filtering out *FutureWarning*, *PendingDeprecationWarning*.
        """
        warnings.simplefilter("default",
                              (FutureWarning,
                               PendingDeprecationWarning,
                               ImportWarning,
                               DeprecationWarning))

    @staticmethod
    def _format_str(s):
        """
        Returns ``s`` or ``'s'`` depending on the type.
        """
        if hasattr(s, "replace"):
            return "'{0}'".format(s)
        else:
            return s

    def assertNotEmpty(self, x):
        """
        Checks that *x* is not empty.
        """
        if x is None or (hasattr(x, "__len__") and len(x) == 0):
            raise AssertionError("x is empty")

    def assertEmpty(self, x, none_allowed=True):
        """
        Checks that *x* is empty.
        """
        if not((none_allowed and x is None) or (hasattr(x, "__len__") and len(x) == 0)):
            if isinstance(x, (list, tuple, dict, set)):
                end = min(5, len(x))
                disp = "\n" + '\n'.join(map(str, x[:end]))
            else:
                disp = ""
            raise AssertionError("x is not empty{0}".format(disp))

    def assertGreater(self, x, y, strict=False):  # pylint: disable=W0221
        """
        Checks that ``x >= y``.
        """
        if x < y or (strict and x == y):
            raise AssertionError("x <{2} y with x={0} and y={1}".format(
                ExtTestCase._format_str(x), ExtTestCase._format_str(y),
                "" if strict else "="))

    def assertLesser(self, x, y, strict=False):
        """
        Checks that ``x <= y``.
        """
        if x > y or (strict and x == y):
            raise AssertionError("x >{2} y with x={0} and y={1}".format(
                ExtTestCase._format_str(x), ExtTestCase._format_str(y),
                "" if strict else "="))

    def assertExists(self, name):
        """
        Checks that *name* exists.
        """
        if not os.path.exists(name):
            raise FileNotFoundError("Unable to find '{0}'.".format(name))

    def assertNotExists(self, name):
        """
        Checks that *name* does not exist.
        """
        if os.path.exists(name):
            raise FileNotFoundError("Able to find '{0}'.".format(name))

    def assertEqualDataFrame(self, d1, d2, **kwargs):
        """
        Checks that two dataframes are equal.
        Calls :epkg:`pandas:testing:assert_frame_equal`.
        """
        from pandas.testing import assert_frame_equal
        assert_frame_equal(d1, d2, **kwargs)

    def assertNotEqualDataFrame(self, d1, d2, **kwargs):
        """
        Checks that two dataframes are different.
        Calls :epkg:`pandas:testing:assert_frame_equal`.
        """
        from pandas.testing import assert_frame_equal
        try:
            assert_frame_equal(d1, d2, **kwargs)
        except AssertionError:
            return
        raise AssertionError("Two dataframes are identical.")

    def assertEqualArray(self, d1, d2, **kwargs):
        """
        Checks that two arrays are equal.
        Relies on :epkg:`numpy:testing:assert_almost_equal.html`.
        """
        if d1 is None and d2 is None:
            return
        if d1 is None:
            raise AssertionError("d1 is None, d2 is not")
        if d2 is None:
            raise AssertionError("d1 is not None, d2 is")
        from numpy.testing import assert_almost_equal
        assert_almost_equal(d1, d2, **kwargs)

    def assertEqualSparseArray(self, d1, d2, **kwargs):
        if type(d1) != type(d2):  # pylint: disable=C0123
            raise AssertionError("d1 and d2 have difference types {} != {}.".format(
                type(d1), type(d2)))
        if d1 is None and d2 is None:
            return
        if (hasattr(d1, 'data') and hasattr(d1, 'row') and hasattr(d1, 'col') and
                hasattr(d2, 'data') and hasattr(d2, 'row') and hasattr(d2, 'col')):
            # coo_matrix
            self.assertEqual(d1.shape, d2.shape)
            self.assertEqualArray(d1.data, d2.data)
            self.assertEqualArray(d1.row, d2.row)
            self.assertEqualArray(d1.col, d2.col)
            return
        if (hasattr(d1, 'data') and hasattr(d1, 'indices') and hasattr(d1, 'indptr') and
                hasattr(d2, 'data') and hasattr(d2, 'indices') and hasattr(d2, 'indptr')):
            # coo_matrix
            self.assertEqual(d1.shape, d2.shape)
            self.assertEqualArray(d1.data, d2.data)
            self.assertEqualArray(d1.indices, d2.indices)
            self.assertEqualArray(d1.indptr, d2.indptr)
            return
        raise NotImplementedError("Comparison not implemented for types {} and {}.".format(
            type(d1), type(d2)))

    def assertNotEqualArray(self, d1, d2, **kwargs):
        """
        Checks that two arrays are equal.
        Relies on :epkg:`numpy:testing:assert_almost_equal.html`.
        """
        if d1 is None and d2 is None:
            raise AssertionError("d1 and d2 are equal to None")
        if d1 is None or d2 is None:
            return
        from numpy.testing import assert_almost_equal
        try:
            assert_almost_equal(d1, d2, **kwargs)
        except AssertionError:
            return
        raise AssertionError("Two arrays are identical.")

    def assertEqualNumber(self, d1, d2, **kwargs):
        """
        Checks that two numbers are equal.
        """
        from numpy import number
        if not isinstance(d1, (int, float, decimal.Decimal, number)):
            raise TypeError('d1 is not a number but {0}'.format(type(d1)))
        if not isinstance(d2, (int, float, decimal.Decimal, number)):
            raise TypeError('d2 is not a number but {0}'.format(type(d2)))
        diff = abs(float(d1 - d2))
        mi = float(min(abs(d1), abs(d2)))
        tol = kwargs.get('precision', None)
        if tol is None:
            if diff != 0:
                raise AssertionError("d1 != d2: {0} != {1}".format(d1, d2))
        else:
            if mi == 0:
                if diff > tol:
                    raise AssertionError(
                        "d1 != d2: {0} != {1} +/- {2}".format(d1, d2, tol))
            else:
                rel = diff / mi
                if rel > tol:
                    raise AssertionError(
                        "d1 != d2: {0} != {1} +/- {2}".format(d1, d2, tol))

    def assertRaise(self, fct, exc=None, msg=None):
        """
        Checks that function *fct* with no parameter
        raises an exception of a given type.

        @param      fct     function to test (no parameter)
        @param      exc     exception type to catch (None for all)
        @param      msg     error message to check (None for no message to check)
        """
        try:
            fct()
        except Exception as e:
            if exc is None:
                return
            elif isinstance(e, exc):
                if msg is None:
                    return
                if msg not in str(e):
                    raise AssertionError(
                        "Function '{0}' raise exception with wrong message '{1}' (must contain '{2}').".format(fct, e, msg))
                return
            raise AssertionError(
                "Function '{0}' does not raise exception '{1}' but '{2}' of type '{3}'.".format(fct, exc, e, type(e)))
        raise AssertionError(
            "Function '{0}' does not raise exception.".format(fct))

    def capture(self, fct):
        """
        Runs a function and capture standard otuput and error.
        """
        sout = StringIO()
        serr = StringIO()
        with redirect_stdout(sout):
            with redirect_stderr(serr):
                res = fct()
        return res, sout.getvalue(), serr.getvalue()

    def assertStartsWith(self, sub, whole):
        """
        Checks that string *sub* starts with *whole*.
        """
        if not whole.startswith(sub):
            if len(whole) > len(sub) * 2:
                whole = whole[:len(sub) * 2]
            raise AssertionError(
                "'{1}' does not start with '{0}'".format(sub, whole))

    def assertNotStartsWith(self, sub, whole):
        """
        Checks that string *sub* does not start with *whole*.
        """
        if whole.startswith(sub):
            if len(whole) > len(sub) * 2:
                whole = whole[:len(sub) * 2]
            raise AssertionError(
                "'{1}' starts with '{0}'".format(sub, whole))

    def assertEndsWith(self, sub, whole):
        """
        Checks that string *sub* ends with *whole*.
        """
        if not whole.endswith(sub):
            if len(whole) > len(sub) * 2:
                whole = whole[-len(sub) * 2:]
            raise AssertionError(
                "'{1}' does not end with '{0}'".format(sub, whole))

    def assertNotEndsWith(self, sub, whole):
        """
        Checks that string *sub* does not end with *whole*.
        """
        if whole.endswith(sub):
            if len(whole) > len(sub) * 2:
                whole = whole[-len(sub) * 2:]
            raise AssertionError(
                "'{1}' ends with '{0}'".format(sub, whole))

    def assertEqual(self, a, b):  # pylint: disable=W0221
        """
        Checks that ``a == b``.
        """
        if a is None and b is not None:
            raise AssertionError("a is None, b is not")
        if a is not None and b is None:
            raise AssertionError("a is not None, b is")
        try:
            unittest.TestCase.assertEqual(self, a, b)
        except ValueError as e:
            if "The truth value of a DataFrame is ambiguous" in str(e) or \
               "The truth value of an array with more than one element is ambiguous." in str(e):
                with warnings.catch_warnings():
                    warnings.filterwarnings("ignore", category=ImportWarning)
                    import pandas
                if isinstance(a, pandas.DataFrame) and isinstance(b, pandas.DataFrame):
                    self.assertEqualDataFrame(a, b)
                    return
                import numpy
                if isinstance(a, numpy.ndarray) and isinstance(b, numpy.ndarray):
                    self.assertEqualArray(a, b)
                    return
            raise AssertionError("Unable to check equality for types {0} and {1}".format(
                type(a), type(b))) from e

    def assertNotEqual(self, a, b):  # pylint: disable=W0221
        """
        Checks that ``a != b``.
        """
        if a is None and b is None:
            raise AssertionError("a is None, b is too")
        if a is None and b is not None:
            return
        if a is not None and b is None:
            return
        try:
            unittest.TestCase.assertNotEqual(self, a, b)
        except ValueError as e:
            if "Can only compare identically-labeled DataFrame objects" in str(e) or \
               "The truth value of a DataFrame is ambiguous." in str(e) or \
               "The truth value of an array with more than one element is ambiguous." in str(e):
                with warnings.catch_warnings():
                    warnings.filterwarnings("ignore", category=ImportWarning)
                    import pandas
                if isinstance(a, pandas.DataFrame) and isinstance(b, pandas.DataFrame):
                    self.assertNotEqualDataFrame(a, b)
                    return
                import numpy
                if isinstance(a, numpy.ndarray) and isinstance(b, numpy.ndarray):
                    self.assertNotEqualArray(a, b)
                    return
            raise e

    def assertEqualFloat(self, a, b, precision=1e-5):
        """
        Checks that ``abs(a-b) < precision``.
        """
        mi = min(abs(a), abs(b))
        if mi == 0:
            d = abs(a - b)
            self.assertLesser(d, precision)
        else:
            r = float(abs(a - b)) / mi
            self.assertLesser(r, precision)

    def assertCallable(self, fct):
        """
        Checks that *fct* is callable.
        """
        if not callable(fct):
            raise AssertionError("fct is not callable: {0}".format(type(fct)))

    def assertEqualDict(self, a, b):
        """
        Checks that ``a == b``.
        """
        if not isinstance(a, dict):
            raise TypeError('a is not dict but {0}'.format(type(a)))
        if not isinstance(b, dict):
            raise TypeError('b is not dict but {0}'.format(type(b)))
        rows = []
        for key in sorted(b):
            if key not in a:
                rows.append("** Added key '{0}' in b".format(key))
            else:
                if a[key] != b[key]:
                    rows.append(
                        "** Value != for key '{0}': != id({1}) != id({2})\n==1 {3}\n==2 {4}".format(
                            key, id(a[key]), id(b[key]), a[key], b[key]))
        for key in sorted(a):
            if key not in b:
                rows.append("** Removed key '{0}' in a".format(key))
        if len(rows) > 0:
            raise AssertionError(
                "Dictionaries are different\n{0}".format('\n'.join(rows)))

    def fLOG(self, *args, **kwargs):
        """
        Prints out some information.
        @see fn fLOG.
        """
        # delayed import
        from ..loghelper import fLOG as _flog
        _flog(*args, **kwargs)

    def profile(self, fct, sort='cumulative', rootrem=None):
        """
        Profiles the execution of a function.

        @param      fct     function to profile
        @param      sort    see `sort_stats <https://docs.python.org/3/library/profile.html#pstats.Stats.sort_stats>`_
        @param      rootrem root to remove in filenames
        @return             statistics text dump
        """
        return profile(fct, sort=sort, rootrem=rootrem)

    def read_file(self, filename, mode='r', encoding="utf-8"):
        """
        Returns the content of a file.

        @param      filename    filename
        @param      encoding    encoding
        @param      mode        reading mode
        @return                 content
        """
        self.assertExists(filename)
        with open(filename, mode, encoding=encoding) as f:
            return f.read()

    def write_file(self, filename, content, mode='w', encoding='utf-8'):
        """
        Writes the content of a file.

        @param      filename    filename
        @param      content     content to write
        @param      encoding    encoding
        @param      mode        reading mode
        @return                 content
        """
        with open(filename, mode, encoding=encoding) as f:
            return f.write(content)


def skipif_appveyor(msg):
    """
    Skips a unit test if it runs on :epkg:`appveyor`.
    """
    if is_travis_or_appveyor() != 'appveyor':
        return lambda x: x
    msg = 'Test does not work on appveyor due to: ' + msg
    return unittest.skip(msg)


def skipif_travis(msg):
    """
    Skips a unit test if it runs on :epkg:`travis`.
    """
    if is_travis_or_appveyor() != 'travis':
        return lambda x: x
    msg = 'Test does not work on travis due to: ' + msg
    return unittest.skip(msg)


def skipif_circleci(msg):
    """
    Skips a unit test if it runs on :epkg:`circleci`.
    """
    if is_travis_or_appveyor() != 'circleci':
        return lambda x: x
    msg = 'Test does not work on circleci due to: ' + msg
    return unittest.skip(msg)


def skipif_azure(msg):
    """
    Skips a unit test if it runs on :epkg:`azure pipeline`.
    """
    if is_travis_or_appveyor() != 'azurepipe':
        return lambda x: x
    msg = 'Test does not work on azure pipeline due to: ' + msg
    return unittest.skip(msg)


def skipif_azure_linux(msg):
    """
    Skips a unit test if it runs on :epkg:`azure pipeline` on :epkg:`linux`.
    """
    if not sys.platform.startswith('lin') and is_travis_or_appveyor() != 'azurepipe':
        return lambda x: x
    msg = 'Test does not work on azure pipeline (linux) due to: ' + msg
    return unittest.skip(msg)


def skipif_azure_macosx(msg):
    """
    Skips a unit test if it runs on :epkg:`azure pipeline` on :epkg:`linux`.
    """
    if not sys.platform.startswith('darwin') and is_travis_or_appveyor() != 'azurepipe':
        return lambda x: x
    msg = 'Test does not work on azure pipeline (macosx) due to: ' + msg
    return unittest.skip(msg)


def skipif_linux(msg):
    """
    Skips a unit test if it runs on :epkg:`linux`.

    .. versionadded:: 1.7
    """
    if not sys.platform.startswith('lin'):
        return lambda x: x
    msg = 'Test does not work on travis due to: ' + msg
    return unittest.skip(msg)


def skipif_vless(version, msg):
    """
    Skips a unit test if the version is stricly below *version* (tuple).

    .. versionadded:: 1.7
    """
    if sys.version_info[:3] >= version:
        return lambda x: x
    msg = 'Python {} < {}: {}'.format(sys.version_info[:3], version, msg)
    return unittest.skip(msg)


def unittest_require_at_least(mod, version, msg=""):
    """
    Skips a unit test if the version of one module
    is not at least the provided version.

    @param      mod     module (the module must have an attribute ``__version__``)
    @param      version expected version or more recent
    @param      msg     message

    .. versionadded:: 1.9
    """
    v = getattr(mod, '__version__', None)
    if v is None:
        raise RuntimeError("Module '{}' has no version.".format(mod))
    if compare_module_version(v, version) >= 0:
        return lambda x: x
    msg = "Module '{}'  is older than '{}' (= '{}'). {}".format(
        mod, version, v, msg)
    return unittest.skip(msg)
