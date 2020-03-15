# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..brains import BRAINSAlignMSP


def test_BRAINSAlignMSP_inputs():
    input_map = dict(
        BackgroundFillValue=dict(argstr="--BackgroundFillValue %s",),
        OutputresampleMSP=dict(argstr="--OutputresampleMSP %s", hash_files=False,),
        args=dict(argstr="%s",),
        environ=dict(nohash=True, usedefault=True,),
        inputVolume=dict(argstr="--inputVolume %s", extensions=None,),
        interpolationMode=dict(argstr="--interpolationMode %s",),
        mspQualityLevel=dict(argstr="--mspQualityLevel %d",),
        numberOfThreads=dict(argstr="--numberOfThreads %d",),
        rescaleIntensities=dict(argstr="--rescaleIntensities ",),
        rescaleIntensitiesOutputRange=dict(
            argstr="--rescaleIntensitiesOutputRange %s", sep=",",
        ),
        resultsDir=dict(argstr="--resultsDir %s", hash_files=False,),
        trimRescaledIntensities=dict(argstr="--trimRescaledIntensities %f",),
        verbose=dict(argstr="--verbose ",),
        writedebuggingImagesLevel=dict(argstr="--writedebuggingImagesLevel %d",),
    )
    inputs = BRAINSAlignMSP.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_BRAINSAlignMSP_outputs():
    output_map = dict(OutputresampleMSP=dict(extensions=None,), resultsDir=dict(),)
    outputs = BRAINSAlignMSP.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
