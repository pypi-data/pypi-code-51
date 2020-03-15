# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..registration import Register


def test_Register_inputs():
    input_map = dict(
        args=dict(argstr="%s",),
        curv=dict(argstr="-curv", requires=["in_smoothwm"],),
        environ=dict(nohash=True, usedefault=True,),
        in_smoothwm=dict(copyfile=True, extensions=None,),
        in_sulc=dict(copyfile=True, extensions=None, mandatory=True,),
        in_surf=dict(
            argstr="%s", copyfile=True, extensions=None, mandatory=True, position=-3,
        ),
        out_file=dict(argstr="%s", extensions=None, genfile=True, position=-1,),
        subjects_dir=dict(),
        target=dict(argstr="%s", extensions=None, mandatory=True, position=-2,),
    )
    inputs = Register.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_Register_outputs():
    output_map = dict(out_file=dict(extensions=None,),)
    outputs = Register.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
