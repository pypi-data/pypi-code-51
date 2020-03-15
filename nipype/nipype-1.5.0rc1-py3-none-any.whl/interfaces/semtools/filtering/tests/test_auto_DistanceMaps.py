# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..featuredetection import DistanceMaps


def test_DistanceMaps_inputs():
    input_map = dict(
        args=dict(argstr="%s",),
        environ=dict(nohash=True, usedefault=True,),
        inputLabelVolume=dict(argstr="--inputLabelVolume %s", extensions=None,),
        inputMaskVolume=dict(argstr="--inputMaskVolume %s", extensions=None,),
        inputTissueLabel=dict(argstr="--inputTissueLabel %d",),
        outputVolume=dict(argstr="--outputVolume %s", hash_files=False,),
    )
    inputs = DistanceMaps.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_DistanceMaps_outputs():
    output_map = dict(outputVolume=dict(extensions=None,),)
    outputs = DistanceMaps.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
