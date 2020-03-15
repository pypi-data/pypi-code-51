# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..preprocess import SliceTiming


def test_SliceTiming_inputs():
    input_map = dict(
        in_files=dict(copyfile=False, field="scans", mandatory=True,),
        matlab_cmd=dict(),
        mfile=dict(usedefault=True,),
        num_slices=dict(field="nslices", mandatory=True,),
        out_prefix=dict(field="prefix", usedefault=True,),
        paths=dict(),
        ref_slice=dict(field="refslice", mandatory=True,),
        slice_order=dict(field="so", mandatory=True,),
        time_acquisition=dict(field="ta", mandatory=True,),
        time_repetition=dict(field="tr", mandatory=True,),
        use_mcr=dict(),
        use_v8struct=dict(min_ver="8", usedefault=True,),
    )
    inputs = SliceTiming.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_SliceTiming_outputs():
    output_map = dict(timecorrected_files=dict(),)
    outputs = SliceTiming.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
