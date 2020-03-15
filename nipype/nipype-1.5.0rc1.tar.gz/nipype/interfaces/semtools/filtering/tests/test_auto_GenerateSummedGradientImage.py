# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..featuredetection import GenerateSummedGradientImage


def test_GenerateSummedGradientImage_inputs():
    input_map = dict(
        MaximumGradient=dict(argstr="--MaximumGradient ",),
        args=dict(argstr="%s",),
        environ=dict(nohash=True, usedefault=True,),
        inputVolume1=dict(argstr="--inputVolume1 %s", extensions=None,),
        inputVolume2=dict(argstr="--inputVolume2 %s", extensions=None,),
        numberOfThreads=dict(argstr="--numberOfThreads %d",),
        outputFileName=dict(argstr="--outputFileName %s", hash_files=False,),
    )
    inputs = GenerateSummedGradientImage.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_GenerateSummedGradientImage_outputs():
    output_map = dict(outputFileName=dict(extensions=None,),)
    outputs = GenerateSummedGradientImage.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
