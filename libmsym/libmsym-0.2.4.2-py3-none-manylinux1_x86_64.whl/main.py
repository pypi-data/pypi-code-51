#
#  libmsym.py
#  libmsym
#
#  Created by Marcus Johansson on 07/10/15.
#  Copyright (c) 2015 Marcus Johansson.
#
#  Distributed under the MIT License ( See LICENSE file or copy at http://opensource.org/licenses/MIT )
#
import os
import sys
from ctypes import *
from ctypes.util import find_library
from enum import Enum
from copy import copy
from . import _libmsym_install_location, export

_lib = None
BASEDIR = os.path.dirname(os.path.abspath(__file__))


@export
class Error(Exception):
    def __init__(self, value, details=""):
        super().__init__(value)
        self.value = value
        self.details = details

    def __str__(self):
        return repr(self.value) + ": " + repr(self.details)

    def __repr__(self):
        return self.__str__()


try:
    import numpy as np
except ImportError:
    np = None


@export
class SymmetryOperation(Structure):

    NONE = 0,
    HORIZONTAL = 1
    VERTICAL = 2
    DIHEDRAL = 3

    IDENTITY = 0,
    PROPER_ROTATION = 1
    IMPROPER_ROTATION = 2
    REFLECTION = 3
    INVERSION = 4

    _names = ["E", "C", "S", "\u03C3", "i"]

    _proper_rotation_type_names = ["", "", "'", "''"]
    _reflection_type_names = ["", "h", "v", "d"]

    _fields_ = [("type", c_int),
                ("order", c_int),
                ("power", c_int),
                ("orientation", c_int),
                ("_v", (c_double*3)),
                ("conjugacy_class", c_int)]

    @property
    def vector(self):
        return self._v[0:3]

    def __str__(self):
        orientation = ""
        order = ""
        power = ""
        axis = ""
        if self.type == self.PROPER_ROTATION and self.order == 2:
            orientation = self._proper_rotation_type_names[self.orientation]
        elif self.type == self.REFLECTION:
            orientation = self._reflection_type_names[self.orientation]
            axis = " with normal vector " + repr(self.vector)

        if self.type in [self.PROPER_ROTATION, self.IMPROPER_ROTATION]:
            order = str(self.order)
            power = "^" + str(self.power)
            axis = " around " + repr(self.vector)

        return __name__ + "." + self.__class__.__name__ + "( " + self._names[self.type] + order + orientation + power + axis + ", conjugacy class: " + str(self.conjugacy_class) + " )"

    def __repr__(self):
        return self.__str__()


@export
class Element(Structure):
    _fields_ = [("_id", c_void_p),
                ("mass", c_double),
                ("_v", c_double*3),
                ("charge", c_int),
                ("_name", c_char*4)]

    @property
    def coordinates(self):
        return self._v[0:3]

    @coordinates.setter
    def coordinates(self, coordinates):
        self._v = (c_double*3)(*coordinates)

    @property
    def name(self):
        return self._name.decode()

    @name.setter
    def name(self, name):
        self._name = name.encode('ascii')


class _RealSphericalHarmonic(Structure):
    _fields_ = [("n", c_int),
                ("l", c_int),
                ("m", c_int)]


class _BasisFunctionUnion(Union):
    _fields_ = [("_rsh", _RealSphericalHarmonic)]


@export
class BasisFunction(Structure):
    _fields_ = [("_id", c_void_p),
                ("_type", c_int),
                ("_element", POINTER(Element)),
                ("_f", _BasisFunctionUnion),
                ("_name", c_char*8)]

    def __init__(self, element=None):
        if element == None:
            raise Error("Basis function requires an element")
        super().__init__()
        self.element = element

    def _set_element_pointer(self, element):
        self._element = pointer(element)

    @property
    def name(self):
        return self._name.decode()

    @name.setter
    def name(self, name):
        self._name = name.encode('ascii')


@export
class RealSphericalHarmonic(BasisFunction):
    def __init__(self, element=None, n=0, l=0, m=0, name=""):
        super().__init__(element=element)
        self._type = 0
        self._f._rsh.n = n
        self._f._rsh.l = l
        self._f._rsh.m = m
        self.name = name

    @property
    def n(self):
        return self._f._rsh.n

    @n.setter
    def n(self, n):
        self._f._rsh.n = n

    @property
    def l(self):
        return self._f._rsh.l

    @l.setter
    def l(self, n):
        self._f._rsh.n = l

    @property
    def m(self):
        return self._f._rsh.m

    @m.setter
    def m(self, n):
        self._f._rsh.n = m


class SALC(Structure):
    _fields_ = [("_d", c_int),
                ("_fl", c_int),
                ("_pf", POINTER(c_double)),
                ("_f", POINTER(POINTER(BasisFunction)))]

    _pf_array = None
    basis_functions = []

    def _update_basis_functions(self, basis_function_addresses, basis):
        self.basis_functions = [basis[basis_function_addresses.index(
            addressof(p.contents))] for p in self._f[0:self._fl]]

    # @property
    # def partner_functions(self):
    #    if self._pf_array is None:
    #        pf = cast(self._pf,POINTER(c_double*self._fl))
    #        self._pf_array = [f[0:self._fl] for f in pf[0:self._d]]
    #
    #    return self._pf_array

    @property
    def partner_functions(self):
        if np is None:
            raise ImportError("numpy is not available.")

        if self._pf_array is None:
            self._pf_array = np.ctypeslib.as_array(
                self._pf, shape=(self._d, self._fl))

        return self._pf_array


@export
class SubrepresentationSpace(Structure):
    _fields_ = [("symmetry_species", c_int),
                ("_salc_length", c_int),
                ("_salcs", POINTER(SALC))]

    _salcarray = None

    @property
    def salcs(self):
        if self._salcarray is None:
            self._salcarray = self._salcs[0:self._salc_length]
        return self._salcarray


@export
class PartnerFunction(Structure):
    _fields_ = [("index", c_int),
                ("dim", c_int)]


@export
class SymmetrySpecies(Structure):
    _fields_ = [("_d", c_int),
                ("_r", c_int),
                ("_name", c_char*8)]

    @property
    def dim(self):
        return self._d

    @property
    def reducible(self):
        return self._r > 1

    @property
    def name(self):
        return self._name.decode()


class _Thresholds(Structure):
    _fields_ = [("zero", c_double),
                ("geometry", c_double),
                ("angle", c_double),
                ("equivalence", c_double),
                ("eigfact", c_double),
                ("permutation", c_double),
                ("orthogonalization", c_double)]


@export
class CharacterTable(Structure):
    _fields_ = [("_d", c_int),
                ("_classc", POINTER(c_int)),
                ("_sops", POINTER(POINTER(SymmetryOperation))),
                ("_s", POINTER(SymmetrySpecies)),
                ("_table", POINTER(c_double))]

    _table_array = None
    _class_count_array = None
    _symmetry_species = None

    @property
    def table(self):
        if np is None:
            raise ImportError("numpy is not available.")

        if self._table_array is None:
            self._table_array = np.ctypeslib.as_array(
                self._table, shape=(self._d, self._d))

        return self._table_array

    @property
    def class_count(self):
        if self._class_count_array is None:
            self._class_count_array = self._classc[0:self._d]
        return self._class_count_array

    def _update_symmetry_operations(self, symmetry_operations):
        addresses = [addressof(sop) for sop in symmetry_operations]
        self.symmetry_operations = [symmetry_operations[addresses.index(
            addressof(sop.contents))] for sop in self._sops[0:self._d]]

    @property
    def symmetry_species(self):
        if self._symmetry_species is None:
            self._symmetry_species = self._s[0:self._d]

        return self._symmetry_species


class _ReturnCode(c_int):

    SUCCESS = 0
    INVALID_INPUT = -1
    INVALID_CONTEXT = -2
    INVALID_THRESHOLD = -3
    INVALID_ELEMENTS = -4
    INVALID_BASIS = -5
    INVALID_POINT_GROUP = -6
    INVALID_EQUIVALENCE_SET = -7
    INVALID_PERMUTATION = -8
    INVALID_GEOMETRY = -9
    INVALID_CHARACTER_TABLE = -10
    INVALID_SUBSPACE = -11
    INVALID_SUBGROUPS = -12
    INVALID_AXES = -13
    SYMMETRY_ERROR = -14
    PERMUTATION_ERROR = -15
    POINT_GROUP_ERROR = -16
    SYMMETRIZATION_ERROR = -17
    SUBSPACE_ERROR = -18

    def __str__(self):
        # init is not called on the return type so we can't contruct data on creation, don't decode details here, may be too late
        error_string = _lib.msymErrorString(self.value).decode()
        return repr(error_string)

    def __repr__(self):
        return self.__str__()


def init(library_location=None):

    if(library_location is None):
        raise Error("Cannot find libmsym shared library")

    global _lib

    _lib = CDLL(library_location)

    _Context = POINTER(type('msym_context', (Structure,), {}))

    _lib.msymErrorString.argtypes = [c_int]
    _lib.msymErrorString.restype = c_char_p

    _lib.msymCreateContext.restype = _Context
    _lib.msymCreateContext.argtypes = []

    _lib.msymGetDefaultThresholds.restype = POINTER(_Thresholds)
    _lib.msymGetDefaultThresholds.argtypes = []

    _lib.msymSetThresholds.restype = _ReturnCode
    _lib.msymSetThresholds.argtypes = [_Context, POINTER(_Thresholds)]

    _lib.msymReleaseContext.restype = _ReturnCode
    _lib.msymReleaseContext.argtypes = [_Context]

    _lib.msymGetErrorDetails.restype = c_char_p
    _lib.msymGetErrorDetails.argtypes = []

    _lib.msymFindSymmetry.restype = _ReturnCode
    _lib.msymFindSymmetry.argtypes = [_Context]

    _lib.msymSetPointGroupByName.restype = _ReturnCode
    _lib.msymSetPointGroupByName.argtypes = [_Context, c_char_p]

    _lib.msymGetPointGroupName.restype = _ReturnCode
    _lib.msymGetPointGroupName.argtypes = [_Context, c_int, c_char_p]

    _lib.msymSetElements.restype = _ReturnCode
    _lib.msymSetElements.argtypes = [_Context, c_int, POINTER(Element)]

    _lib.msymGenerateElements.restype = _ReturnCode
    _lib.msymGenerateElements.argtypes = [_Context, c_int, POINTER(Element)]

    _lib.msymGetElements.restype = _ReturnCode
    _lib.msymGetElements.argtypes = [
        _Context, POINTER(c_int), POINTER(POINTER(Element))]

    _lib.msymGetSymmetryOperations.restype = _ReturnCode
    _lib.msymGetSymmetryOperations.argtypes = [
        _Context, POINTER(c_int), POINTER(POINTER(SymmetryOperation))]

    _lib.msymSymmetrizeElements.restype = _ReturnCode
    _lib.msymSymmetrizeElements.argtypes = [_Context]

    _lib.msymSetBasisFunctions.restype = _ReturnCode
    _lib.msymSetBasisFunctions.argtypes = [
        _Context, c_int, POINTER(BasisFunction)]

    _lib.msymGetBasisFunctions.restype = _ReturnCode
    _lib.msymGetBasisFunctions.argtypes = [
        _Context, POINTER(c_int), POINTER(POINTER(BasisFunction))]

    _lib.msymGetSubrepresentationSpaces.restype = _ReturnCode
    _lib.msymGetSubrepresentationSpaces.argtypes = [
        _Context, POINTER(c_int), POINTER(POINTER(SubrepresentationSpace))]

    _lib.msymGetCharacterTable.restype = _ReturnCode
    _lib.msymGetCharacterTable.argtypes = [
        _Context, POINTER(POINTER(CharacterTable))]

    if np is None:
        _SALCsMatrix = c_void_p
        _SALCsSpecies = POINTER(c_int)
        _NPDArray = POINTER(c_double)
    else:
        _SALCsMatrix = np.ctypeslib.ndpointer(
            dtype=np.float64, ndim=2, flags='C_CONTIGUOUS')
        _SALCsSpecies = np.ctypeslib.ndpointer(
            dtype=np.int32, ndim=1, flags='C_CONTIGUOUS')
        _NPDArray = np.ctypeslib.ndpointer(
            dtype=np.float64, ndim=1, flags='C_CONTIGUOUS')

    _lib.msymSymmetrySpeciesComponents.restype = _ReturnCode
    _lib.msymSymmetrySpeciesComponents.argtypes = [
        _Context, c_int, _NPDArray, c_int, _NPDArray]

    _lib.msymGetSALCs.restype = _ReturnCode
    _lib.msymGetSALCs.argtypes = [
        _Context, c_int, _SALCsMatrix, _SALCsSpecies, POINTER(PartnerFunction)]

    _lib.msymSymmetrizeWavefunctions.restype = _ReturnCode
    _lib.msymSymmetrizeWavefunctions.argtypes = [
        _Context, c_int, _SALCsMatrix, _SALCsSpecies, POINTER(PartnerFunction)]


_libmsym_location = find_library('msym')

if _libmsym_location is None:
    # _libmsym_location = _libmsym_install_location
    if sys.platform == 'linux':
        _libmsym_location = os.path.join(BASEDIR, 'libmsym.so')
    elif sys.platform == 'darwin':
        _libmsym_location = os.path.join(BASEDIR, 'libmsym.dylib')
    else:
        raise NotImplementedError(sys.platform + ' not supported')

if not (_libmsym_location is None):
    init(_libmsym_location)


@export
class Context(object):

    _ctx = None

    def __init__(self, elements=[], basis_functions=[], point_group=""):
        if(_lib is None):
            raise Error("Shared library not loaded")

        self._elements = []
        self._basis_functions = []
        self._point_group = None
        self._subrepresentation_spaces = None
        self._character_table = None
        self._ctx = _lib.msymCreateContext()
        if not self._ctx:
            raise RuntimeError('Failed to create libmsym context')
        pthresholds = _lib.msymGetDefaultThresholds()
        default_thresholds = pthresholds.contents
        if default_thresholds is None:
            raise RuntimeError('Failed get libmsym default thresholds')
        self._thresholds = copy(default_thresholds)
        if len(elements) > 0:
            self._set_elements(elements)
        if len(basis_functions) > 0:
            self._set_basis_functions(basis_functions)
        if len(point_group) > 0:
            self._set_point_group(point_group)
            self.find_symmetry()

    def __del__(self):

        self._destruct()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._destruct()

    def _destruct(self):
        if self._ctx:
            _lib.msymReleaseContext(self._ctx)
        self._ctx = None

    @staticmethod
    def _assert_success(error):
        if not error.value == _ReturnCode.SUCCESS:
            raise Error(error, details=_lib.msymGetErrorDetails().decode())

    def _get_basis_function_addresses(self):
        if not self._ctx:
            raise RuntimeError
        cbfs = POINTER(BasisFunction)()
        csize = c_int(0)
        self._assert_success(_lib.msymGetBasisFunctions(
            self._ctx, byref(csize), byref(cbfs)))
        return [addressof(bf) for bf in cbfs[0:csize.value]]

    def _set_elements(self, elements):
        if not self._ctx:
            raise RuntimeError
        self._subrepresentation_spaces = None
        self._character_table = None
        self._salcs = None
        self._basis_functions = []
        size = len(elements)
        element_array = (Element*size)(*elements)
        self._assert_success(_lib.msymSetElements(
            self._ctx, size, element_array))
        self._element_array = element_array
        self._elements = elements

    def _set_point_group(self, point_group):
        if not self._ctx:
            raise RuntimeError
        self._subrepresentation_spaces = None
        self._character_table = None
        self._salcs = None
        cname = c_char_p(point_group.encode('ascii'))
        self._assert_success(_lib.msymSetPointGroupByName(self._ctx, cname))
        self._update_symmetry_operations()

    def _set_basis_functions(self, basis_functions):
        if not self._ctx:
            raise RuntimeError
        self._subrepresentation_spaces = None
        self._salcs = None
        size = len(basis_functions)
        for bf in basis_functions:
            bf._set_element_pointer(
                self._element_array[self._elements.index(bf.element)])

        self._assert_success(_lib.msymSetBasisFunctions(
            self._ctx, size, (BasisFunction*size)(*basis_functions)))
        self._basis_functions = basis_functions
        if not self._point_group is None:
            self._update_symmetry_operations()
            self._update_character_table()

    def _update_elements(self):
        if not self._ctx:
            raise RuntimeError
        celements = POINTER(Element)()
        csize = c_int(0)
        self._assert_success(_lib.msymGetElements(
            self._ctx, byref(csize), byref(celements)))
        self._elements_array = celements
        self._elements = celements[0:csize.value]

    def _update_symmetry_operations(self):
        if not self._ctx:
            raise RuntimeError
        csops = POINTER(SymmetryOperation)()
        csize = c_int(0)
        self._assert_success(_lib.msymGetSymmetryOperations(
            self._ctx, byref(csize), byref(csops)))
        self._symmetry_operations = csops[0:csize.value]

    def _update_point_group(self):
        if not self._ctx:
            raise RuntimeError
        cname = (c_char*8)()
        self._assert_success(_lib.msymGetPointGroupName(
            self._ctx, sizeof(cname), cname))
        self._point_group = cname.value.decode()

    def _update_subrepresentation_spaces(self):
        if not self._ctx:
            raise RuntimeError
        basis_function_addresses = self._get_basis_function_addresses()
        csrs = POINTER(SubrepresentationSpace)()
        csize = c_int(0)
        self._assert_success(_lib.msymGetSubrepresentationSpaces(
            self._ctx, byref(csize), byref(csrs)))
        srs = csrs[0:csize.value]
        for s in srs:
            for salc in s.salcs:
                salc._update_basis_functions(
                    basis_function_addresses, self._basis_functions)
        self._subrepresentation_spaces = srs

    def _update_character_table(self):
        if not self._ctx:
            raise RuntimeError
        cct = POINTER(CharacterTable)()
        self._assert_success(_lib.msymGetCharacterTable(self._ctx, byref(cct)))
        self._character_table = cct.contents
        self._character_table._update_symmetry_operations(
            self._symmetry_operations)

    def _update_salcs(self):
        if not self._ctx:
            raise RuntimeError
        if np is None:
            raise ImportError("numpy is not available.")
        csize = len(self._basis_functions)
        partner_functions = (PartnerFunction*csize)()
        salcs = np.zeros((csize, csize), dtype=np.float64)
        species = np.zeros((csize), dtype=np.int32)
        self._assert_success(_lib.msymGetSALCs(
            self._ctx, csize, salcs, species, partner_functions))
        self._salcs = (salcs, species, partner_functions[0:csize])

    def set_thresholds(self, **kwargs):
        for key in kwargs.keys():
            if not key in ['zero', 'geometry', 'angle', 'equivalence',
                           'eigfact', 'permutation', 'orthogonalization']:
                raise Error('Unrecognized threshold argument')
            setattr(self._thresholds, key, kwargs[key])
        self._assert_success(_lib.msymSetThresholds(
            self._ctx, pointer(self._thresholds)))

    @property
    def elements(self):
        return self._elements

    @elements.setter
    def elements(self, elements):
        self._set_elements(elements)

    @property
    def basis_functions(self):
        return self._basis_functions

    @basis_functions.setter
    def basis_functions(self, basis_functions):
        self._set_basis_functions(basis_functions)

    @property
    def point_group(self):
        return self._point_group

    @point_group.setter
    def point_group(self, point_group):
        self._set_point_group(point_group)

    @property
    def symmetry_operations(self):
        return self._symmetry_operations

    def find_symmetry(self):
        if not self._ctx:
            raise RuntimeError
        self._assert_success(_lib.msymFindSymmetry(self._ctx))
        self._update_point_group()
        self._update_symmetry_operations()
        return self._point_group

    def symmetrize_elements(self):
        if not self._ctx:
            raise RuntimeError
        cerror = c_double(0)
        self._assert_success(
            _lib.msymSymmetrizeElements(self._ctx, byref(cerror)))
        self._update_elements()
        return self._elements

    @property
    def subrepresentation_spaces(self):
        if self._subrepresentation_spaces is None:
            self._update_subrepresentation_spaces()

        return self._subrepresentation_spaces

    @property
    def character_table(self):
        if self._character_table is None:
            self._update_character_table()

        return self._character_table

    @property
    def salcs(self):
        if self._salcs is None:
            self._update_salcs()

        return self._salcs

    def symmetrize_wavefunctions(self, m):
        if not self._ctx:
            raise RuntimeError
        if np is None:
            raise ImportError("numpy is not available.")
        csize = len(self._basis_functions)
        (d1, d2) = m.shape
        if not (d1 == csize and d2 == csize):
            raise ValueError("Must provide a " + str(csize) + "x" + str(csize))
        wf = np.ascontiguousarray(m, dtype=np.float64)
        partner_functions = (PartnerFunction*csize)()
        species = np.zeros((csize), dtype=np.int32)
        self._assert_success(_lib.msymSymmetrizeWavefunctions(
            self._ctx, csize, wf, species, partner_functions))
        return (wf, species, partner_functions[0:csize])

    def generate_elements(self, elements):
        if not self._ctx:
            raise RuntimeError
        self._subrepresentation_spaces = None
        self._character_table = None
        self._salcs = None
        self._element_array = None
        self._basis_functions = []
        self._elements = []
        size = len(elements)
        element_array = (Element*size)(*elements)
        self._assert_success(_lib.msymGenerateElements(
            self._ctx, size, element_array))
        self._update_elements()
        return self._elements

    def symmetry_species_components(self, wf):

        wf_size = len(wf)
        if not wf_size == len(self.basis_functions):
            raise ValueError("Must provide an array of length " +
                             str(len(self.basis_functions)))
        species_size = self.character_table._d
        species = np.zeros((species_size), dtype=np.float64)
        wf = np.ascontiguousarray(wf, dtype=np.float64)
        self._assert_success(_lib.msymSymmetrySpeciesComponents(
            self._ctx, wf_size, wf, species_size, species))
        return species
