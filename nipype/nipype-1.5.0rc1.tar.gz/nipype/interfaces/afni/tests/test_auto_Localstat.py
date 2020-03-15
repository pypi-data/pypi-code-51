# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..utils import Localstat


def test_Localstat_inputs():
    input_map = dict(
        args=dict(argstr="%s",),
        automask=dict(argstr="-automask",),
        environ=dict(nohash=True, usedefault=True,),
        grid_rmode=dict(argstr="-grid_rmode %s", requires=["reduce_restore_grid"],),
        in_file=dict(argstr="%s", extensions=None, mandatory=True, position=-1,),
        mask_file=dict(argstr="-mask %s", extensions=None,),
        neighborhood=dict(argstr="-nbhd '%s(%s)'", mandatory=True,),
        nonmask=dict(argstr="-use_nonmask",),
        num_threads=dict(nohash=True, usedefault=True,),
        out_file=dict(
            argstr="-prefix %s",
            extensions=None,
            keep_extension=True,
            name_source="in_file",
            name_template="%s_localstat",
            position=0,
        ),
        outputtype=dict(),
        overwrite=dict(argstr="-overwrite",),
        quiet=dict(argstr="-quiet",),
        reduce_grid=dict(
            argstr="-reduce_grid %s", xor=["reduce_restore_grid", "reduce_max_vox"],
        ),
        reduce_max_vox=dict(
            argstr="-reduce_max_vox %s", xor=["reduce_restore_grid", "reduce_grid"],
        ),
        reduce_restore_grid=dict(
            argstr="-reduce_restore_grid %s", xor=["reduce_max_vox", "reduce_grid"],
        ),
        stat=dict(argstr="-stat %s...", mandatory=True,),
    )
    inputs = Localstat.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_Localstat_outputs():
    output_map = dict(out_file=dict(extensions=None,),)
    outputs = Localstat.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
