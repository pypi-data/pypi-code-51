# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..brainsuite import ThicknessPVC


def test_ThicknessPVC_inputs():
    input_map = dict(
        args=dict(argstr="%s",),
        environ=dict(nohash=True, usedefault=True,),
        subjectFilePrefix=dict(argstr="%s", mandatory=True,),
    )
    inputs = ThicknessPVC.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
