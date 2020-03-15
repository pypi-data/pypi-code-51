# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..reconst import ConstrainedSphericalDeconvolution


def test_ConstrainedSphericalDeconvolution_inputs():
    input_map = dict(
        algorithm=dict(argstr="%s", mandatory=True, position=-8,),
        args=dict(argstr="%s",),
        bval_scale=dict(argstr="-bvalue_scaling %s",),
        csf_odf=dict(argstr="%s", extensions=None, position=-1,),
        csf_txt=dict(argstr="%s", extensions=None, position=-2,),
        environ=dict(nohash=True, usedefault=True,),
        gm_odf=dict(argstr="%s", extensions=None, position=-3,),
        gm_txt=dict(argstr="%s", extensions=None, position=-4,),
        grad_file=dict(argstr="-grad %s", extensions=None, xor=["grad_fsl"],),
        grad_fsl=dict(argstr="-fslgrad %s %s", xor=["grad_file"],),
        in_bval=dict(extensions=None,),
        in_bvec=dict(argstr="-fslgrad %s %s", extensions=None,),
        in_dirs=dict(argstr="-directions %s", extensions=None,),
        in_file=dict(argstr="%s", extensions=None, mandatory=True, position=-7,),
        mask_file=dict(argstr="-mask %s", extensions=None,),
        max_sh=dict(argstr="-lmax %s", sep=",",),
        nthreads=dict(argstr="-nthreads %d", nohash=True,),
        shell=dict(argstr="-shell %s", sep=",",),
        wm_odf=dict(
            argstr="%s", extensions=None, mandatory=True, position=-5, usedefault=True,
        ),
        wm_txt=dict(argstr="%s", extensions=None, mandatory=True, position=-6,),
    )
    inputs = ConstrainedSphericalDeconvolution.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_ConstrainedSphericalDeconvolution_outputs():
    output_map = dict(
        csf_odf=dict(argstr="%s", extensions=None,),
        gm_odf=dict(argstr="%s", extensions=None,),
        wm_odf=dict(argstr="%s", extensions=None,),
    )
    outputs = ConstrainedSphericalDeconvolution.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
