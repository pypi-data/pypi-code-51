# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..csv import CSVReader


def test_CSVReader_inputs():
    input_map = dict(
        header=dict(usedefault=True,), in_file=dict(extensions=None, mandatory=True,),
    )
    inputs = CSVReader.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_CSVReader_outputs():
    output_map = dict()
    outputs = CSVReader.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
