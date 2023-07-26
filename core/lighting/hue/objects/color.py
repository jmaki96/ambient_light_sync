from dataclasses import dataclass
from typing import List, Optional

from dataclasses_json import DataClassJsonMixin

from core.lighting.hue.enums import GamutType


@dataclass
class _CIEXYGamut(DataClassJsonMixin):
    """A CIE XY gamut position. 
    
    NOTE: https://spec.oneapi.io/oneipl/0.6/concepts/cie-chromaticity-diagram-and-color-gamut.html"""

    x: float # [0.0, 1.0]
    y: float # [0.0, 1.0]


@dataclass
class _RGBGamut(DataClassJsonMixin):
    red: _CIEXYGamut
    green: _CIEXYGamut
    blue: _CIEXYGamut


@dataclass
class Color(DataClassJsonMixin):
    """How light Color data is structured in the Hue API."""
    
    xy: _CIEXYGamut
    gamut_type: Optional[GamutType] = None
    gamut: Optional[_RGBGamut] = None
