# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..model import ContrastMgr


def test_ContrastMgr_inputs():
    input_map = dict(
        args=dict(argstr="%s",),
        contrast_num=dict(argstr="-cope",),
        corrections=dict(copyfile=False, extensions=None, mandatory=True,),
        dof_file=dict(argstr="", copyfile=False, extensions=None, mandatory=True,),
        environ=dict(nohash=True, usedefault=True,),
        fcon_file=dict(argstr="-f %s", extensions=None,),
        output_type=dict(),
        param_estimates=dict(argstr="", copyfile=False, mandatory=True,),
        sigmasquareds=dict(
            argstr="", copyfile=False, extensions=None, mandatory=True, position=-2,
        ),
        suffix=dict(argstr="-suffix %s",),
        tcon_file=dict(argstr="%s", extensions=None, mandatory=True, position=-1,),
    )
    inputs = ContrastMgr.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_ContrastMgr_outputs():
    output_map = dict(
        copes=dict(),
        fstats=dict(),
        neffs=dict(),
        tstats=dict(),
        varcopes=dict(),
        zfstats=dict(),
        zstats=dict(),
    )
    outputs = ContrastMgr.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
