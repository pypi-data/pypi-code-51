# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..base import Select


def test_Select_inputs():
    input_map = dict(index=dict(mandatory=True,), inlist=dict(mandatory=True,),)
    inputs = Select.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_Select_outputs():
    output_map = dict(out=dict(),)
    outputs = Select.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
