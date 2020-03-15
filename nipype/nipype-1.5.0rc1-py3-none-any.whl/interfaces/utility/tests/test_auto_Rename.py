# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..base import Rename


def test_Rename_inputs():
    input_map = dict(
        format_string=dict(mandatory=True,),
        in_file=dict(extensions=None, mandatory=True,),
        keep_ext=dict(),
        parse_string=dict(),
        use_fullpath=dict(usedefault=True,),
    )
    inputs = Rename.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_Rename_outputs():
    output_map = dict(out_file=dict(extensions=None,),)
    outputs = Rename.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
