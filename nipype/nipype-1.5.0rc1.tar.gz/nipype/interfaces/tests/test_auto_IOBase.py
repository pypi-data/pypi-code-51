# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..io import IOBase


def test_IOBase_inputs():
    input_map = dict()
    inputs = IOBase.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
