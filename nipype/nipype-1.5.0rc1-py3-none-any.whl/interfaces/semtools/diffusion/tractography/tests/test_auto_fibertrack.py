# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..fibertrack import fibertrack


def test_fibertrack_inputs():
    input_map = dict(
        args=dict(argstr="%s",),
        environ=dict(nohash=True, usedefault=True,),
        forbidden_label=dict(argstr="--forbidden_label %d",),
        force=dict(argstr="--force ",),
        input_roi_file=dict(argstr="--input_roi_file %s", extensions=None,),
        input_tensor_file=dict(argstr="--input_tensor_file %s", extensions=None,),
        max_angle=dict(argstr="--max_angle %f",),
        min_fa=dict(argstr="--min_fa %f",),
        output_fiber_file=dict(argstr="--output_fiber_file %s", hash_files=False,),
        really_verbose=dict(argstr="--really_verbose ",),
        source_label=dict(argstr="--source_label %d",),
        step_size=dict(argstr="--step_size %f",),
        target_label=dict(argstr="--target_label %d",),
        verbose=dict(argstr="--verbose ",),
        whole_brain=dict(argstr="--whole_brain ",),
    )
    inputs = fibertrack.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_fibertrack_outputs():
    output_map = dict(output_fiber_file=dict(extensions=None,),)
    outputs = fibertrack.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
