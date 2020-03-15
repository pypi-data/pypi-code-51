# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..minc import BigAverage


def test_BigAverage_inputs():
    input_map = dict(
        args=dict(argstr="%s",),
        clobber=dict(argstr="--clobber", usedefault=True,),
        environ=dict(nohash=True, usedefault=True,),
        input_files=dict(argstr="%s", mandatory=True, position=-2, sep=" ",),
        output_file=dict(
            argstr="%s",
            extensions=None,
            genfile=True,
            hash_files=False,
            name_source=["input_files"],
            name_template="%s_bigaverage.mnc",
            position=-1,
        ),
        output_float=dict(argstr="--float",),
        robust=dict(argstr="-robust",),
        sd_file=dict(
            argstr="--sdfile %s",
            extensions=None,
            hash_files=False,
            name_source=["input_files"],
            name_template="%s_bigaverage_stdev.mnc",
        ),
        tmpdir=dict(argstr="-tmpdir %s",),
        verbose=dict(argstr="--verbose",),
    )
    inputs = BigAverage.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_BigAverage_outputs():
    output_map = dict(
        output_file=dict(extensions=None,), sd_file=dict(extensions=None,),
    )
    outputs = BigAverage.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
