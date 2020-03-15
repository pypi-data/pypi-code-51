# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..bru2nii import Bru2


def test_Bru2_inputs():
    input_map = dict(
        actual_size=dict(argstr="-a",),
        append_protocol_name=dict(argstr="-p",),
        args=dict(argstr="%s",),
        compress=dict(argstr="-z",),
        environ=dict(nohash=True, usedefault=True,),
        force_conversion=dict(argstr="-f",),
        input_dir=dict(argstr="%s", mandatory=True, position=-1,),
        output_filename=dict(argstr="-o %s", genfile=True,),
    )
    inputs = Bru2.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_Bru2_outputs():
    output_map = dict(nii_file=dict(extensions=None,),)
    outputs = Bru2.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
