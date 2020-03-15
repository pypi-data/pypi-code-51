# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..fix import Training


def test_Training_inputs():
    input_map = dict(
        args=dict(argstr="%s",),
        environ=dict(nohash=True, usedefault=True,),
        loo=dict(argstr="-l", position=2,),
        mel_icas=dict(argstr="%s", copyfile=False, position=-1,),
        trained_wts_filestem=dict(argstr="%s", position=1,),
    )
    inputs = Training.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_Training_outputs():
    output_map = dict(trained_wts_file=dict(extensions=None,),)
    outputs = Training.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
