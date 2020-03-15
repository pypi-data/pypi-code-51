# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..preprocess import SliceTimer


def test_SliceTimer_inputs():
    input_map = dict(
        args=dict(argstr="%s",),
        custom_order=dict(argstr="--ocustom=%s", extensions=None,),
        custom_timings=dict(argstr="--tcustom=%s", extensions=None,),
        environ=dict(nohash=True, usedefault=True,),
        global_shift=dict(argstr="--tglobal",),
        in_file=dict(argstr="--in=%s", extensions=None, mandatory=True, position=0,),
        index_dir=dict(argstr="--down",),
        interleaved=dict(argstr="--odd",),
        out_file=dict(
            argstr="--out=%s", extensions=None, genfile=True, hash_files=False,
        ),
        output_type=dict(),
        slice_direction=dict(argstr="--direction=%d",),
        time_repetition=dict(argstr="--repeat=%f",),
    )
    inputs = SliceTimer.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_SliceTimer_outputs():
    output_map = dict(slice_time_corrected_file=dict(extensions=None,),)
    outputs = SliceTimer.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
