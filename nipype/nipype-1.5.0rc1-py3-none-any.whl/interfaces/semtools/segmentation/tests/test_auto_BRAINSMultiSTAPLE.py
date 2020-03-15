# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..specialized import BRAINSMultiSTAPLE


def test_BRAINSMultiSTAPLE_inputs():
    input_map = dict(
        args=dict(argstr="%s",),
        environ=dict(nohash=True, usedefault=True,),
        inputCompositeT1Volume=dict(
            argstr="--inputCompositeT1Volume %s", extensions=None,
        ),
        inputLabelVolume=dict(argstr="--inputLabelVolume %s...",),
        inputTransform=dict(argstr="--inputTransform %s...",),
        labelForUndecidedPixels=dict(argstr="--labelForUndecidedPixels %d",),
        outputConfusionMatrix=dict(
            argstr="--outputConfusionMatrix %s", hash_files=False,
        ),
        outputMultiSTAPLE=dict(argstr="--outputMultiSTAPLE %s", hash_files=False,),
        resampledVolumePrefix=dict(argstr="--resampledVolumePrefix %s",),
        skipResampling=dict(argstr="--skipResampling ",),
    )
    inputs = BRAINSMultiSTAPLE.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_BRAINSMultiSTAPLE_outputs():
    output_map = dict(
        outputConfusionMatrix=dict(extensions=None,),
        outputMultiSTAPLE=dict(extensions=None,),
    )
    outputs = BRAINSMultiSTAPLE.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
