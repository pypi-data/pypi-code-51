# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..segmentation import BRAINSTalairach


def test_BRAINSTalairach_inputs():
    input_map = dict(
        AC=dict(argstr="--AC %s", sep=",",),
        ACisIndex=dict(argstr="--ACisIndex ",),
        IRP=dict(argstr="--IRP %s", sep=",",),
        IRPisIndex=dict(argstr="--IRPisIndex ",),
        PC=dict(argstr="--PC %s", sep=",",),
        PCisIndex=dict(argstr="--PCisIndex ",),
        SLA=dict(argstr="--SLA %s", sep=",",),
        SLAisIndex=dict(argstr="--SLAisIndex ",),
        args=dict(argstr="%s",),
        environ=dict(nohash=True, usedefault=True,),
        inputVolume=dict(argstr="--inputVolume %s", extensions=None,),
        outputBox=dict(argstr="--outputBox %s", hash_files=False,),
        outputGrid=dict(argstr="--outputGrid %s", hash_files=False,),
    )
    inputs = BRAINSTalairach.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_BRAINSTalairach_outputs():
    output_map = dict(
        outputBox=dict(extensions=None,), outputGrid=dict(extensions=None,),
    )
    outputs = BRAINSTalairach.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
