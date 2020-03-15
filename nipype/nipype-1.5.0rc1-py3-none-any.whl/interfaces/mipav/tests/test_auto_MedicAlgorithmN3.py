# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..developer import MedicAlgorithmN3


def test_MedicAlgorithmN3_inputs():
    input_map = dict(
        args=dict(argstr="%s",),
        environ=dict(nohash=True, usedefault=True,),
        inAutomatic=dict(argstr="--inAutomatic %s",),
        inEnd=dict(argstr="--inEnd %f",),
        inField=dict(argstr="--inField %f",),
        inInput=dict(argstr="--inInput %s", extensions=None,),
        inKernel=dict(argstr="--inKernel %f",),
        inMaximum=dict(argstr="--inMaximum %d",),
        inSignal=dict(argstr="--inSignal %f",),
        inSubsample=dict(argstr="--inSubsample %f",),
        inWeiner=dict(argstr="--inWeiner %f",),
        null=dict(argstr="--null %s",),
        outInhomogeneity=dict(argstr="--outInhomogeneity %s", hash_files=False,),
        outInhomogeneity2=dict(argstr="--outInhomogeneity2 %s", hash_files=False,),
        xDefaultMem=dict(argstr="-xDefaultMem %d",),
        xMaxProcess=dict(argstr="-xMaxProcess %d", usedefault=True,),
        xPrefExt=dict(argstr="--xPrefExt %s",),
    )
    inputs = MedicAlgorithmN3.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_MedicAlgorithmN3_outputs():
    output_map = dict(
        outInhomogeneity=dict(extensions=None,),
        outInhomogeneity2=dict(extensions=None,),
    )
    outputs = MedicAlgorithmN3.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
