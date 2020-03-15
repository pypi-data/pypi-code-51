# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..utils import NwarpCat


def test_NwarpCat_inputs():
    input_map = dict(
        args=dict(argstr="%s",),
        environ=dict(nohash=True, usedefault=True,),
        expad=dict(argstr="-expad %d",),
        in_files=dict(argstr="%s", mandatory=True, position=-1,),
        interp=dict(argstr="-interp %s", usedefault=True,),
        inv_warp=dict(argstr="-iwarp",),
        num_threads=dict(nohash=True, usedefault=True,),
        out_file=dict(
            argstr="-prefix %s",
            extensions=None,
            name_source="in_files",
            name_template="%s_NwarpCat",
        ),
        outputtype=dict(),
        space=dict(argstr="-space %s",),
        verb=dict(argstr="-verb",),
    )
    inputs = NwarpCat.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_NwarpCat_outputs():
    output_map = dict(out_file=dict(extensions=None,),)
    outputs = NwarpCat.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
