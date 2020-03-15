# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..tensors import ConstrainedSphericalDeconvolution


def test_ConstrainedSphericalDeconvolution_inputs():
    input_map = dict(
        args=dict(argstr="%s",),
        debug=dict(argstr="-debug",),
        directions_file=dict(argstr="-directions %s", extensions=None, position=-2,),
        encoding_file=dict(argstr="-grad %s", extensions=None, position=1,),
        environ=dict(nohash=True, usedefault=True,),
        filter_file=dict(argstr="-filter %s", extensions=None, position=-2,),
        in_file=dict(argstr="%s", extensions=None, mandatory=True, position=-3,),
        iterations=dict(argstr="-niter %s",),
        lambda_value=dict(argstr="-lambda %s",),
        mask_image=dict(argstr="-mask %s", extensions=None, position=2,),
        maximum_harmonic_order=dict(argstr="-lmax %s",),
        normalise=dict(argstr="-normalise", position=3,),
        out_filename=dict(argstr="%s", extensions=None, genfile=True, position=-1,),
        response_file=dict(argstr="%s", extensions=None, mandatory=True, position=-2,),
        threshold_value=dict(argstr="-threshold %s",),
    )
    inputs = ConstrainedSphericalDeconvolution.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_ConstrainedSphericalDeconvolution_outputs():
    output_map = dict(spherical_harmonics_image=dict(extensions=None,),)
    outputs = ConstrainedSphericalDeconvolution.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
