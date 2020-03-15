# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..utils import OneDToolPy


def test_OneDToolPy_inputs():
    input_map = dict(
        args=dict(argstr="%s",),
        censor_motion=dict(argstr="-censor_motion %f %s",),
        censor_prev_TR=dict(argstr="-censor_prev_TR",),
        demean=dict(argstr="-demean",),
        derivative=dict(argstr="-derivative",),
        environ=dict(nohash=True, usedefault=True,),
        in_file=dict(argstr="-infile %s", extensions=None, mandatory=True,),
        out_file=dict(
            argstr="-write %s", extensions=None, xor=["show_cormat_warnings"],
        ),
        outputtype=dict(),
        py27_path=dict(usedefault=True,),
        set_nruns=dict(argstr="-set_nruns %d",),
        show_censor_count=dict(argstr="-show_censor_count",),
        show_cormat_warnings=dict(
            argstr="-show_cormat_warnings |& tee %s",
            extensions=None,
            position=-1,
            xor=["out_file"],
        ),
        show_indices_interest=dict(argstr="-show_indices_interest",),
        show_trs_run=dict(argstr="-show_trs_run %d",),
        show_trs_uncensored=dict(argstr="-show_trs_uncensored %s",),
    )
    inputs = OneDToolPy.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_OneDToolPy_outputs():
    output_map = dict(out_file=dict(extensions=None,),)
    outputs = OneDToolPy.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
