# -*- coding: utf-8 -*-
# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
"""
AFNI_ is a software suite for the analysis and display of anatomical and functional MRI data.

.. include:: ../../../doc/links_names.txt

"""

from .base import Info
from .preprocess import (
    AlignEpiAnatPy,
    Allineate,
    Automask,
    AutoTcorrelate,
    AutoTLRC,
    Bandpass,
    BlurInMask,
    BlurToFWHM,
    ClipLevel,
    DegreeCentrality,
    Despike,
    Detrend,
    ECM,
    Fim,
    Fourier,
    Hist,
    LFCD,
    Maskave,
    Means,
    OutlierCount,
    QualityIndex,
    ROIStats,
    Retroicor,
    Seg,
    SkullStrip,
    TCorr1D,
    TCorrMap,
    TCorrelate,
    TNorm,
    TProject,
    TShift,
    TSmooth,
    Volreg,
    Warp,
    QwarpPlusMinus,
    Qwarp,
)
from .svm import SVMTest, SVMTrain
from .utils import (
    ABoverlap,
    AFNItoNIFTI,
    Autobox,
    Axialize,
    BrickStat,
    Bucket,
    Calc,
    Cat,
    CatMatvec,
    CenterMass,
    ConvertDset,
    Copy,
    Dot,
    Edge3,
    Eval,
    FWHMx,
    LocalBistat,
    Localstat,
    MaskTool,
    Merge,
    Notes,
    NwarpApply,
    NwarpAdjust,
    NwarpCat,
    OneDToolPy,
    Refit,
    ReHo,
    Resample,
    TCat,
    TCatSubBrick,
    TStat,
    To3D,
    Unifize,
    Undump,
    ZCutUp,
    GCOR,
    Zcat,
    Zeropad,
)
from .model import Deconvolve, Remlfit, Synthesize
