# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..utils import Complex


def test_Complex_inputs():
    input_map = dict(
        args=dict(argstr="%s",),
        complex_cartesian=dict(
            argstr="-complex",
            position=1,
            xor=[
                "real_polar",
                "real_cartesian",
                "complex_cartesian",
                "complex_polar",
                "complex_split",
                "complex_merge",
            ],
        ),
        complex_in_file=dict(argstr="%s", extensions=None, position=2,),
        complex_in_file2=dict(argstr="%s", extensions=None, position=3,),
        complex_merge=dict(
            argstr="-complexmerge",
            position=1,
            xor=[
                "real_polar",
                "real_cartesian",
                "complex_cartesian",
                "complex_polar",
                "complex_split",
                "complex_merge",
                "start_vol",
                "end_vol",
            ],
        ),
        complex_out_file=dict(
            argstr="%s",
            extensions=None,
            genfile=True,
            position=-3,
            xor=[
                "complex_out_file",
                "magnitude_out_file",
                "phase_out_file",
                "real_out_file",
                "imaginary_out_file",
                "real_polar",
                "real_cartesian",
            ],
        ),
        complex_polar=dict(
            argstr="-complexpolar",
            position=1,
            xor=[
                "real_polar",
                "real_cartesian",
                "complex_cartesian",
                "complex_polar",
                "complex_split",
                "complex_merge",
            ],
        ),
        complex_split=dict(
            argstr="-complexsplit",
            position=1,
            xor=[
                "real_polar",
                "real_cartesian",
                "complex_cartesian",
                "complex_polar",
                "complex_split",
                "complex_merge",
            ],
        ),
        end_vol=dict(argstr="%d", position=-1,),
        environ=dict(nohash=True, usedefault=True,),
        imaginary_in_file=dict(argstr="%s", extensions=None, position=3,),
        imaginary_out_file=dict(
            argstr="%s",
            extensions=None,
            genfile=True,
            position=-3,
            xor=[
                "complex_out_file",
                "magnitude_out_file",
                "phase_out_file",
                "real_polar",
                "complex_cartesian",
                "complex_polar",
                "complex_split",
                "complex_merge",
            ],
        ),
        magnitude_in_file=dict(argstr="%s", extensions=None, position=2,),
        magnitude_out_file=dict(
            argstr="%s",
            extensions=None,
            genfile=True,
            position=-4,
            xor=[
                "complex_out_file",
                "real_out_file",
                "imaginary_out_file",
                "real_cartesian",
                "complex_cartesian",
                "complex_polar",
                "complex_split",
                "complex_merge",
            ],
        ),
        output_type=dict(),
        phase_in_file=dict(argstr="%s", extensions=None, position=3,),
        phase_out_file=dict(
            argstr="%s",
            extensions=None,
            genfile=True,
            position=-3,
            xor=[
                "complex_out_file",
                "real_out_file",
                "imaginary_out_file",
                "real_cartesian",
                "complex_cartesian",
                "complex_polar",
                "complex_split",
                "complex_merge",
            ],
        ),
        real_cartesian=dict(
            argstr="-realcartesian",
            position=1,
            xor=[
                "real_polar",
                "real_cartesian",
                "complex_cartesian",
                "complex_polar",
                "complex_split",
                "complex_merge",
            ],
        ),
        real_in_file=dict(argstr="%s", extensions=None, position=2,),
        real_out_file=dict(
            argstr="%s",
            extensions=None,
            genfile=True,
            position=-4,
            xor=[
                "complex_out_file",
                "magnitude_out_file",
                "phase_out_file",
                "real_polar",
                "complex_cartesian",
                "complex_polar",
                "complex_split",
                "complex_merge",
            ],
        ),
        real_polar=dict(
            argstr="-realpolar",
            position=1,
            xor=[
                "real_polar",
                "real_cartesian",
                "complex_cartesian",
                "complex_polar",
                "complex_split",
                "complex_merge",
            ],
        ),
        start_vol=dict(argstr="%d", position=-2,),
    )
    inputs = Complex.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_Complex_outputs():
    output_map = dict(
        complex_out_file=dict(extensions=None,),
        imaginary_out_file=dict(extensions=None,),
        magnitude_out_file=dict(extensions=None,),
        phase_out_file=dict(extensions=None,),
        real_out_file=dict(extensions=None,),
    )
    outputs = Complex.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
