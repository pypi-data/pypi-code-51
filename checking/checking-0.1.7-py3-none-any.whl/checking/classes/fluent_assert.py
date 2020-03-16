from typing import Iterable, Sized, Sequence

from checking.asserts import *
from .basic_listener import short


class FluentAssert:
    """
    Класс для гибких, читаемых проверок, которые можно собирать в цепочки (при желании разделяя AND)
    При провале одной из проверок, тест падает и другие условия не проверяются!
    Пример:

    verify(my_list).is_not_none().AND.is_a(list).AND.contains(2).AND.is_sorted()

    """

    def __init__(self, obj: Any):
        """
        При инициализации принимаем объект, который нужно проверять. Не предполагается, что это будет класс или тип!
        :param obj:
        """
        self.__actual = obj
        self._t = type(self.__actual)
        # Строковое представление объекта в сокращенном виде (не более 50 символов)
        self.str = short(self.__actual)
        # Ссылка на самого себя для читаемой последовательности проверок
        self.AND = self

    def is_a(self, obj: Any):
        """
        Проверяем, является ли наш объект и данный одним и тем же объектом. Аналогично проверке a is b
        :param obj: объект для проверки
        :return: None
        """
        if self.__actual is not obj:
            raise AssertionError(f'"{self.str}"{self._t} is not "{short(obj)}"{type(obj)}')
        return self

    def is_not(self, obj: Any):
        """
        Проверяем, что проверяемый объект не является тем же объектом, что и данный. Аналогично проверке a is not b
        :param obj: объект для проверки
        :return: None
        """
        if self.__actual is obj:
            raise AssertionError(f'"{self.str}"{self._t} is the same as "{short(obj)}"{type(obj)}')
        return self

    def child_of(self, type_: Type):
        """
        Проверяем, является ли наш объект конкретным классом(типом) или его наследником
        :param type_: тип для проверки
        :return: None
        """
        self._check_is_type(type_)
        if issubclass(type(self.__actual), type_):
            return self
        raise AssertionError(f'"{self.str}"{self._t} is not sub-class of {type_}')

    def is_none(self):
        is_none(self.__actual)
        return self

    def is_not_none(self):
        not_none(self.__actual)
        return self

    def is_true(self):
        is_true(self.__actual)
        return self

    def is_false(self):
        is_false(self.__actual)
        return self

    def equal(self, obj: Any):
        equals(self.__actual, obj)
        return self

    def not_equal(self, obj: Any):
        not_equals(self.__actual, obj)
        return self

    def less_than(self, obj: Any):
        """
        Проверка, что проверяемый объект меньше, чем данный
        :param obj: объект для сравнения
        :return:
        """
        self._check_same_type(obj)
        if self.__actual >= obj:
            raise AssertionError(f'"{self.str}" is not less than "{short(obj)}"!')
        return self

    def greater_than(self, obj: Any):
        self._check_same_type(obj)
        if self.__actual <= obj:
            raise AssertionError(f'"{self.str}" is not greater than "{short(obj)}"!')
        return self

    def length_equal_to_length_of(self, obj: Sized):
        self._check_has_len(self.__actual)
        self._check_has_len(obj)
        len_ = len(self.__actual)
        len_obj = len(obj)
        if len_ != len_obj:
            raise AssertionError(f'Length of object is {len_}, it is not equal to {len_obj}')
        return self

    def length_equal_to(self, obj: int):
        self._check_has_len(self.__actual)
        len_ = len(self.__actual)
        if type(obj) is not int:
            raise TestBrokenException(f'Length can be only int type, not {type(obj)}')
        if len_ != obj:
            raise AssertionError(f'Length of object is {len_}, it is not equal to {obj}')
        return self

    def length_less_than_length_of(self, obj: Sized):
        self._check_has_len(self.__actual)
        self._check_has_len(obj)
        len_ = len(self.__actual)
        len_obj = len(obj)
        if len_ >= len_obj:
            raise AssertionError(f'Length of "{self.str}" is {len_}, it is not less of "{obj}"({len_obj})')
        return self

    def length_less_than(self, obj: int):
        self._check_has_len(self.__actual)
        len_ = len(self.__actual)
        if type(obj) is not int:
            raise TestBrokenException(f'Length can be only int type, not {type(obj)}')
        if len_ >= obj:
            raise AssertionError(f'Length of object is {len_}, it is not less than {obj}')
        return self

    def length_greater_than_length_of(self, obj: Sized):
        self._check_has_len(self.__actual)
        self._check_has_len(obj)
        len_ = len(self.__actual)
        len_obj = len(obj)
        if len_ <= len_obj:
            raise AssertionError(f'Length of "{self.str}" is {len_}, it is not greater of "{short(obj)}"({len_obj})')
        return self

    def length_greater_than(self, obj: int):
        self._check_has_len(self.__actual)
        len_ = len(self.__actual)
        if type(obj) is not int:
            raise TestBrokenException(f'Length can be only int type, not {type(obj)}')
        if len_ <= obj:
            raise AssertionError(f'Length of object is {len_}, it is not greater than {obj}')
        return self

    def is_sorted(self, reverse_order: bool = False):
        """
        Проверка, что проверяемый объект отсортирован (применимо, только к list/tuple/str и прочим Sequence)
        :param reverse_order: если True то проверяет сортировку в обратном порядке (от большего к меньшему)
        :return:
        """
        if not isinstance(self.__actual, Sequence):
            raise TestBrokenException(f'Only sequences can be checked for sorted, not {self._t}')
        smaller = lambda a, b: a <= b
        bigger = lambda a, b: a >= b
        check = smaller if not reverse_order else bigger
        for index, element in enumerate(self.__actual):
            if index == len(self.__actual) - 1:
                break
            if not check(element, self.__actual[index + 1]):
                raise AssertionError(f'Object "{self.str}" is not sorted!')
        return self

    def contains(self, obj: Any):
        contains(obj, self.__actual)
        return self

    def not_contains(self, obj: Any):
        not_contains(obj, self.__actual)
        return self

    def contains_in_any_order(self, obj: Iterable):
        if not isinstance(obj, Iterable):
            raise TestBrokenException(f'Only Iterables can be argument here, not {type(obj)}')
        for element in obj:
            contains(element, self.__actual)
        return self

    def _check_same_type(self, second):
        if self._t is not type(second):
            raise TestBrokenException('To compare "less" or "greater" both arguments must be the same type!')

    def _check_is_type(self, obj):
        if type(obj) is not type:
            raise TestBrokenException(f'Argument "{obj}"{type(obj)} is not type!')

    def _check_has_len(self, obj):
        try:
            len(obj)
        except TypeError:
            raise TestBrokenException(f'There is no length for "{short(obj)}"{type(obj)}')


def verify(obj: Any) -> FluentAssert:
    return FluentAssert(obj)
