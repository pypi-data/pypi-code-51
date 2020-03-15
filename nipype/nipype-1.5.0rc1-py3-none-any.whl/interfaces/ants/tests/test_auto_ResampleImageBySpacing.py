# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..utils import ResampleImageBySpacing


def test_ResampleImageBySpacing_inputs():
    input_map = dict(
        addvox=dict(argstr="%d", position=6, requires=["apply_smoothing"],),
        apply_smoothing=dict(argstr="%d", position=5,),
        args=dict(argstr="%s",),
        copy_header=dict(mandatory=True, usedefault=True,),
        dimension=dict(argstr="%d", position=1, usedefault=True,),
        environ=dict(nohash=True, usedefault=True,),
        input_image=dict(argstr="%s", extensions=None, mandatory=True, position=2,),
        nn_interp=dict(argstr="%d", position=-1, requires=["addvox"],),
        num_threads=dict(nohash=True, usedefault=True,),
        out_spacing=dict(argstr="%s", mandatory=True, position=4,),
        output_image=dict(
            argstr="%s",
            extensions=None,
            keep_extension=True,
            name_source=["input_image"],
            name_template="%s_resampled",
            position=3,
        ),
    )
    inputs = ResampleImageBySpacing.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_ResampleImageBySpacing_outputs():
    output_map = dict(output_image=dict(extensions=None,),)
    outputs = ResampleImageBySpacing.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
