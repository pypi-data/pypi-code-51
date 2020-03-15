# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..brains import landmarksConstellationAligner


def test_landmarksConstellationAligner_inputs():
    input_map = dict(
        args=dict(argstr="%s",),
        environ=dict(nohash=True, usedefault=True,),
        inputLandmarksPaired=dict(argstr="--inputLandmarksPaired %s", extensions=None,),
        outputLandmarksPaired=dict(
            argstr="--outputLandmarksPaired %s", hash_files=False,
        ),
    )
    inputs = landmarksConstellationAligner.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_landmarksConstellationAligner_outputs():
    output_map = dict(outputLandmarksPaired=dict(extensions=None,),)
    outputs = landmarksConstellationAligner.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
