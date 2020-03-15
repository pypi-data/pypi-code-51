# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..utils import ImageMath


def test_ImageMath_inputs():
    input_map = dict(
        args=dict(argstr="%s",),
        copy_header=dict(usedefault=True,),
        dimension=dict(argstr="%d", position=1, usedefault=True,),
        environ=dict(nohash=True, usedefault=True,),
        num_threads=dict(nohash=True, usedefault=True,),
        op1=dict(argstr="%s", extensions=None, mandatory=True, position=-2,),
        op2=dict(argstr="%s", position=-1,),
        operation=dict(argstr="%s", mandatory=True, position=3,),
        output_image=dict(
            argstr="%s",
            extensions=None,
            keep_extension=True,
            name_source=["op1"],
            name_template="%s_maths",
            position=2,
        ),
    )
    inputs = ImageMath.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_ImageMath_outputs():
    output_map = dict(output_image=dict(extensions=None,),)
    outputs = ImageMath.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
