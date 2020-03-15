# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..tensors import EstimateResponseForSH


def test_EstimateResponseForSH_inputs():
    input_map = dict(
        args=dict(argstr="%s",),
        debug=dict(argstr="-debug",),
        encoding_file=dict(
            argstr="-grad %s", extensions=None, mandatory=True, position=1,
        ),
        environ=dict(nohash=True, usedefault=True,),
        in_file=dict(argstr="%s", extensions=None, mandatory=True, position=-3,),
        mask_image=dict(argstr="%s", extensions=None, mandatory=True, position=-2,),
        maximum_harmonic_order=dict(argstr="-lmax %s",),
        normalise=dict(argstr="-normalise",),
        out_filename=dict(argstr="%s", extensions=None, genfile=True, position=-1,),
        quiet=dict(argstr="-quiet",),
    )
    inputs = EstimateResponseForSH.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_EstimateResponseForSH_outputs():
    output_map = dict(response=dict(extensions=None,),)
    outputs = EstimateResponseForSH.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
