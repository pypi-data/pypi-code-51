# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..confounds import ComputeDVARS


def test_ComputeDVARS_inputs():
    input_map = dict(
        figdpi=dict(usedefault=True,),
        figformat=dict(usedefault=True,),
        figsize=dict(usedefault=True,),
        in_file=dict(extensions=None, mandatory=True,),
        in_mask=dict(extensions=None, mandatory=True,),
        intensity_normalization=dict(usedefault=True,),
        remove_zerovariance=dict(usedefault=True,),
        save_all=dict(usedefault=True,),
        save_nstd=dict(usedefault=True,),
        save_plot=dict(usedefault=True,),
        save_std=dict(usedefault=True,),
        save_vxstd=dict(usedefault=True,),
        series_tr=dict(),
    )
    inputs = ComputeDVARS.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_ComputeDVARS_outputs():
    output_map = dict(
        avg_nstd=dict(),
        avg_std=dict(),
        avg_vxstd=dict(),
        fig_nstd=dict(extensions=None,),
        fig_std=dict(extensions=None,),
        fig_vxstd=dict(extensions=None,),
        out_all=dict(extensions=None,),
        out_nstd=dict(extensions=None,),
        out_std=dict(extensions=None,),
        out_vxstd=dict(extensions=None,),
    )
    outputs = ComputeDVARS.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
