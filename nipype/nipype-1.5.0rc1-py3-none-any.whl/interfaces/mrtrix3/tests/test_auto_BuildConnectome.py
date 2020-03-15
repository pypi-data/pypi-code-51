# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..connectivity import BuildConnectome


def test_BuildConnectome_inputs():
    input_map = dict(
        args=dict(argstr="%s",),
        environ=dict(nohash=True, usedefault=True,),
        in_file=dict(argstr="%s", extensions=None, mandatory=True, position=-3,),
        in_parc=dict(argstr="%s", extensions=None, position=-2,),
        in_scalar=dict(argstr="-image %s", extensions=None,),
        in_weights=dict(argstr="-tck_weights_in %s", extensions=None,),
        keep_unassigned=dict(argstr="-keep_unassigned",),
        metric=dict(argstr="-metric %s",),
        nthreads=dict(argstr="-nthreads %d", nohash=True,),
        out_file=dict(
            argstr="%s", extensions=None, mandatory=True, position=-1, usedefault=True,
        ),
        search_forward=dict(argstr="-assignment_forward_search %f",),
        search_radius=dict(argstr="-assignment_radial_search %f",),
        search_reverse=dict(argstr="-assignment_reverse_search %f",),
        vox_lookup=dict(argstr="-assignment_voxel_lookup",),
        zero_diagonal=dict(argstr="-zero_diagonal",),
    )
    inputs = BuildConnectome.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_BuildConnectome_outputs():
    output_map = dict(out_file=dict(extensions=None,),)
    outputs = BuildConnectome.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
