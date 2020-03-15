# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..specialized import BRAINSCreateLabelMapFromProbabilityMaps


def test_BRAINSCreateLabelMapFromProbabilityMaps_inputs():
    input_map = dict(
        args=dict(argstr="%s",),
        cleanLabelVolume=dict(argstr="--cleanLabelVolume %s", hash_files=False,),
        dirtyLabelVolume=dict(argstr="--dirtyLabelVolume %s", hash_files=False,),
        environ=dict(nohash=True, usedefault=True,),
        foregroundPriors=dict(argstr="--foregroundPriors %s", sep=",",),
        inclusionThreshold=dict(argstr="--inclusionThreshold %f",),
        inputProbabilityVolume=dict(argstr="--inputProbabilityVolume %s...",),
        nonAirRegionMask=dict(argstr="--nonAirRegionMask %s", extensions=None,),
        priorLabelCodes=dict(argstr="--priorLabelCodes %s", sep=",",),
    )
    inputs = BRAINSCreateLabelMapFromProbabilityMaps.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_BRAINSCreateLabelMapFromProbabilityMaps_outputs():
    output_map = dict(
        cleanLabelVolume=dict(extensions=None,),
        dirtyLabelVolume=dict(extensions=None,),
    )
    outputs = BRAINSCreateLabelMapFromProbabilityMaps.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
