# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..io import SelectFiles


def test_SelectFiles_inputs():
    input_map = dict(
        base_directory=dict(),
        force_lists=dict(usedefault=True,),
        raise_on_empty=dict(usedefault=True,),
        sort_filelist=dict(usedefault=True,),
    )
    inputs = SelectFiles.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_SelectFiles_outputs():
    output_map = dict()
    outputs = SelectFiles.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
