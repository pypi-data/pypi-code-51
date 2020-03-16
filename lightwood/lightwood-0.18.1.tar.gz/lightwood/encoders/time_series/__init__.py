from lightwood.encoders.time_series.ts_fresh_ts import TsFreshTsEncoder

default = TsFreshTsEncoder

# Optional encoders
try:
    from lightwood.encoders.time_series.cesium_ts import CesiumTsEncoder
    CesiumTsEncoder = CesiumTsEncoder
except:
    pass
