# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..maths import BinaryMathsInteger


def test_BinaryMathsInteger_inputs():
    input_map = dict(
        args=dict(argstr="%s",),
        environ=dict(nohash=True, usedefault=True,),
        in_file=dict(argstr="%s", extensions=None, mandatory=True, position=2,),
        operand_value=dict(argstr="%d", mandatory=True, position=5,),
        operation=dict(argstr="-%s", mandatory=True, position=4,),
        out_file=dict(
            argstr="%s",
            extensions=None,
            name_source=["in_file"],
            name_template="%s",
            position=-2,
        ),
        output_datatype=dict(argstr="-odt %s", position=-3,),
    )
    inputs = BinaryMathsInteger.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_BinaryMathsInteger_outputs():
    output_map = dict(out_file=dict(extensions=None,),)
    outputs = BinaryMathsInteger.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
