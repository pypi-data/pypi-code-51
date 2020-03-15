# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..imagelabelcombine import ImageLabelCombine


def test_ImageLabelCombine_inputs():
    input_map = dict(
        InputLabelMap_A=dict(argstr="%s", extensions=None, position=-3,),
        InputLabelMap_B=dict(argstr="%s", extensions=None, position=-2,),
        OutputLabelMap=dict(argstr="%s", hash_files=False, position=-1,),
        args=dict(argstr="%s",),
        environ=dict(nohash=True, usedefault=True,),
        first_overwrites=dict(argstr="--first_overwrites ",),
    )
    inputs = ImageLabelCombine.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_ImageLabelCombine_outputs():
    output_map = dict(OutputLabelMap=dict(extensions=None, position=-1,),)
    outputs = ImageLabelCombine.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
