# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..dti import ComputeTensorTrace


def test_ComputeTensorTrace_inputs():
    input_map = dict(
        args=dict(argstr="%s",),
        environ=dict(nohash=True, usedefault=True,),
        in_file=dict(argstr="< %s", extensions=None, mandatory=True, position=1,),
        inputdatatype=dict(argstr="-inputdatatype %s",),
        inputmodel=dict(argstr="-inputmodel %s",),
        out_file=dict(argstr="> %s", extensions=None, genfile=True, position=-1,),
        outputdatatype=dict(argstr="-outputdatatype %s",),
        scheme_file=dict(argstr="%s", extensions=None, position=2,),
    )
    inputs = ComputeTensorTrace.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_ComputeTensorTrace_outputs():
    output_map = dict(trace=dict(extensions=None,),)
    outputs = ComputeTensorTrace.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
