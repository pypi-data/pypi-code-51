#!/usr/bin/python
# -*- coding: utf-8 -*-
from .ancillary_feature import AncillaryFeature  # noqa: F401
from . import af_basic
from . import af_emodulus
from . import af_fl_max_ctc
from . import af_image_contour


#: features whose computation is fast
FEATURES_RAPID = [
    "area_ratio",
    "area_um",
    "aspec",
    "deform",
    "index",
    "time",
]


af_basic.register()
af_emodulus.register()
af_fl_max_ctc.register()
af_image_contour.register()
