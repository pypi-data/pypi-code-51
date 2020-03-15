# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..gtract import gtractCoRegAnatomy


def test_gtractCoRegAnatomy_inputs():
    input_map = dict(
        args=dict(argstr="%s",),
        borderSize=dict(argstr="--borderSize %d",),
        convergence=dict(argstr="--convergence %f",),
        environ=dict(nohash=True, usedefault=True,),
        gradientTolerance=dict(argstr="--gradientTolerance %f",),
        gridSize=dict(argstr="--gridSize %s", sep=",",),
        inputAnatomicalVolume=dict(
            argstr="--inputAnatomicalVolume %s", extensions=None,
        ),
        inputRigidTransform=dict(argstr="--inputRigidTransform %s", extensions=None,),
        inputVolume=dict(argstr="--inputVolume %s", extensions=None,),
        maxBSplineDisplacement=dict(argstr="--maxBSplineDisplacement %f",),
        maximumStepSize=dict(argstr="--maximumStepSize %f",),
        minimumStepSize=dict(argstr="--minimumStepSize %f",),
        numberOfHistogramBins=dict(argstr="--numberOfHistogramBins %d",),
        numberOfIterations=dict(argstr="--numberOfIterations %d",),
        numberOfSamples=dict(argstr="--numberOfSamples %d",),
        numberOfThreads=dict(argstr="--numberOfThreads %d",),
        outputTransformName=dict(argstr="--outputTransformName %s", hash_files=False,),
        relaxationFactor=dict(argstr="--relaxationFactor %f",),
        samplingPercentage=dict(argstr="--samplingPercentage %f",),
        spatialScale=dict(argstr="--spatialScale %d",),
        transformType=dict(argstr="--transformType %s",),
        translationScale=dict(argstr="--translationScale %f",),
        useCenterOfHeadAlign=dict(argstr="--useCenterOfHeadAlign ",),
        useGeometryAlign=dict(argstr="--useGeometryAlign ",),
        useMomentsAlign=dict(argstr="--useMomentsAlign ",),
        vectorIndex=dict(argstr="--vectorIndex %d",),
    )
    inputs = gtractCoRegAnatomy.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_gtractCoRegAnatomy_outputs():
    output_map = dict(outputTransformName=dict(extensions=None,),)
    outputs = gtractCoRegAnatomy.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
