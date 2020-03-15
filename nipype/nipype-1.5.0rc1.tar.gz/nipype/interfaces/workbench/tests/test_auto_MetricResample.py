# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..metric import MetricResample


def test_MetricResample_inputs():
    input_map = dict(
        area_metrics=dict(argstr="-area-metrics", position=5, xor=["area_surfs"],),
        area_surfs=dict(argstr="-area-surfs", position=5, xor=["area_metrics"],),
        args=dict(argstr="%s",),
        current_area=dict(argstr="%s", extensions=None, position=6,),
        current_sphere=dict(argstr="%s", extensions=None, mandatory=True, position=1,),
        environ=dict(nohash=True, usedefault=True,),
        in_file=dict(argstr="%s", extensions=None, mandatory=True, position=0,),
        largest=dict(argstr="-largest", position=10,),
        method=dict(argstr="%s", mandatory=True, position=3,),
        new_area=dict(argstr="%s", extensions=None, position=7,),
        new_sphere=dict(argstr="%s", extensions=None, mandatory=True, position=2,),
        out_file=dict(
            argstr="%s",
            extensions=None,
            keep_extension=True,
            name_source=["new_sphere"],
            name_template="%s.out",
            position=4,
        ),
        roi_metric=dict(argstr="-current-roi %s", extensions=None, position=8,),
        valid_roi_out=dict(argstr="-valid-roi-out", position=9,),
    )
    inputs = MetricResample.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_MetricResample_outputs():
    output_map = dict(out_file=dict(extensions=None,), roi_file=dict(extensions=None,),)
    outputs = MetricResample.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
