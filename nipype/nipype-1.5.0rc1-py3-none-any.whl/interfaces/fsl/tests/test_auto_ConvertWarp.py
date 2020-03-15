# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..utils import ConvertWarp


def test_ConvertWarp_inputs():
    input_map = dict(
        abswarp=dict(argstr="--abs", xor=["relwarp"],),
        args=dict(argstr="%s",),
        cons_jacobian=dict(argstr="--constrainj",),
        environ=dict(nohash=True, usedefault=True,),
        jacobian_max=dict(argstr="--jmax=%f",),
        jacobian_min=dict(argstr="--jmin=%f",),
        midmat=dict(argstr="--midmat=%s", extensions=None,),
        out_abswarp=dict(argstr="--absout", xor=["out_relwarp"],),
        out_file=dict(
            argstr="--out=%s",
            extensions=None,
            name_source=["reference"],
            name_template="%s_concatwarp",
            output_name="out_file",
            position=-1,
        ),
        out_relwarp=dict(argstr="--relout", xor=["out_abswarp"],),
        output_type=dict(),
        postmat=dict(argstr="--postmat=%s", extensions=None,),
        premat=dict(argstr="--premat=%s", extensions=None,),
        reference=dict(argstr="--ref=%s", extensions=None, mandatory=True, position=1,),
        relwarp=dict(argstr="--rel", xor=["abswarp"],),
        shift_direction=dict(argstr="--shiftdir=%s", requires=["shift_in_file"],),
        shift_in_file=dict(argstr="--shiftmap=%s", extensions=None,),
        warp1=dict(argstr="--warp1=%s", extensions=None,),
        warp2=dict(argstr="--warp2=%s", extensions=None,),
    )
    inputs = ConvertWarp.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_ConvertWarp_outputs():
    output_map = dict(out_file=dict(extensions=None,),)
    outputs = ConvertWarp.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
