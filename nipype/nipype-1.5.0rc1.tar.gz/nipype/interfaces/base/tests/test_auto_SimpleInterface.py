# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..core import SimpleInterface


def test_SimpleInterface_inputs():
    input_map = dict()
    inputs = SimpleInterface.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
