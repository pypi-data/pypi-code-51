# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..registration import MRICoreg


def test_MRICoreg_inputs():
    input_map = dict(
        args=dict(argstr="%s",),
        brute_force_limit=dict(argstr="--bf-lim %g", xor=["no_brute_force"],),
        brute_force_samples=dict(argstr="--bf-nsamp %d", xor=["no_brute_force"],),
        conform_reference=dict(argstr="--conf-ref",),
        dof=dict(argstr="--dof %d",),
        environ=dict(nohash=True, usedefault=True,),
        ftol=dict(argstr="--ftol %e",),
        initial_rotation=dict(argstr="--rot %g %g %g",),
        initial_scale=dict(argstr="--scale %g %g %g",),
        initial_shear=dict(argstr="--shear %g %g %g",),
        initial_translation=dict(argstr="--trans %g %g %g",),
        linmintol=dict(argstr="--linmintol %e",),
        max_iters=dict(argstr="--nitersmax %d",),
        no_brute_force=dict(argstr="--no-bf",),
        no_coord_dithering=dict(argstr="--no-coord-dither",),
        no_cras0=dict(argstr="--no-cras0",),
        no_intensity_dithering=dict(argstr="--no-intensity-dither",),
        no_smooth=dict(argstr="--no-smooth",),
        num_threads=dict(argstr="--threads %d",),
        out_lta_file=dict(argstr="--lta %s", usedefault=True,),
        out_params_file=dict(argstr="--params %s",),
        out_reg_file=dict(argstr="--regdat %s",),
        ref_fwhm=dict(argstr="--ref-fwhm",),
        reference_file=dict(
            argstr="--ref %s",
            copyfile=False,
            extensions=None,
            mandatory=True,
            xor=["subject_id"],
        ),
        reference_mask=dict(argstr="--ref-mask %s", position=2,),
        saturation_threshold=dict(argstr="--sat %g",),
        sep=dict(argstr="--sep %s...",),
        source_file=dict(
            argstr="--mov %s", copyfile=False, extensions=None, mandatory=True,
        ),
        source_mask=dict(argstr="--mov-mask",),
        source_oob=dict(argstr="--mov-oob",),
        subject_id=dict(
            argstr="--s %s",
            mandatory=True,
            position=1,
            requires=["subjects_dir"],
            xor=["reference_file"],
        ),
        subjects_dir=dict(argstr="--sd %s",),
    )
    inputs = MRICoreg.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_MRICoreg_outputs():
    output_map = dict(
        out_lta_file=dict(extensions=None,),
        out_params_file=dict(extensions=None,),
        out_reg_file=dict(extensions=None,),
    )
    outputs = MRICoreg.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
