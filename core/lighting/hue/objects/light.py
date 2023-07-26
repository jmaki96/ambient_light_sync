from dataclasses import dataclass
from datetime import datetime
import json
from typing import List, Optional

from dataclasses_json import DataClassJsonMixin

from core.lighting.hue.enums import SupportedDynamicStatus, LightMode, SupportedGradientMode, SignalStatus, SupportedEffect, PowerUpColorMode, PowerUpDimmingMode, PowerUpOnMode, PowerUpPreset, ResourceType
from core.lighting.hue.objects.resource import Resource
from core.lighting.hue.objects.color import Color


@dataclass
class _LightOn(DataClassJsonMixin):
    on: bool

@dataclass
class _LightDimming(DataClassJsonMixin):
    brightness: float  # (0.0, 100.0]
    min_dim_level: Optional[float] = None  # [0.0, 100.0]

@dataclass
class _MirekSchema(DataClassJsonMixin):
    mirek_minimum: int  # [153, 500]
    mirek_maximum: int  # [153, 500]

@dataclass 
class _LightColorTemperature(DataClassJsonMixin):
    mirek: int  # [153, 500]
    mirek_valid: Optional[bool] = None
    mirek_schema: Optional[_MirekSchema] = None

@dataclass
class _LightDynamics(DataClassJsonMixin):
    status: SupportedDynamicStatus
    status_values: List[SupportedDynamicStatus]
    speed: float # [0.0, 1.0]
    speed_valid: bool

@dataclass
class _LightAlert(DataClassJsonMixin):
    action_values: List[str]  # AlertEffectType enum maybe?

@dataclass
class _SignalStatus(DataClassJsonMixin):
    signal: SignalStatus
    estimated_end: datetime

@dataclass
class _LightSignalling(DataClassJsonMixin):
    status: Optional[_SignalStatus] = None

@dataclass
class _LightGradient(DataClassJsonMixin):
    points: List[Color]  # Maximum of 5 can be specified
    mode: SupportedGradientMode
    points_capable: int
    mode_values: List[SupportedGradientMode]
    pixel_count: Optional[int] = None

@dataclass
class _LightEffect(DataClassJsonMixin):
    # effect: SupportedEffect  # This field isn't returned by my lights
    status_values: List[SupportedEffect]
    status: SupportedEffect
    effect_values: List[SupportedEffect]

@dataclass
class _LightTimedEffect(DataClassJsonMixin):
    effect: SupportedEffect
    status_values: List[SupportedEffect]
    status: SupportedEffect
    effect_values: List[SupportedEffect]
    duration: Optional[int] = None  # Seconds

@dataclass
class _PowerUpColor(DataClassJsonMixin):
    mode: PowerUpColorMode
    color_temperature: Optional[_LightColorTemperature] = None
    color: Optional[Color] = None

@dataclass
class _PowerUpDimming(DataClassJsonMixin):
    mode: PowerUpDimmingMode
    dimming: Optional[_LightDimming] = None

@dataclass
class _PowerUpOn(DataClassJsonMixin):
    mode: PowerUpOnMode
    on: Optional[_LightOn] = None

@dataclass
class _LightPowerUp(DataClassJsonMixin):
    preset: PowerUpPreset
    configured: bool
    on: _PowerUpOn
    dimming: _PowerUpDimming
    color: _PowerUpColor

@dataclass
class Light(DataClassJsonMixin):
    """An instance of a Hue LightGet as returned by a call to /resource/light
    """

    type: ResourceType
    id: str
    owner: Resource
    # metadata has been deprecated, so not loading it even if it is available
    on: _LightOn
    mode: LightMode

    alert: Optional[_LightAlert] = None
    color_temperature: Optional[_LightColorTemperature] = None
    color: Optional[Color] = None
    dimming: Optional[_LightDimming] = None
    dynamics: Optional[_LightDynamics] = None
    effects: Optional[_LightEffect] = None
    gradient: Optional[_LightGradient] = None
    signaling: Optional[_LightSignalling] = None
    timed_effects: Optional[_LightTimedEffect] = None
    power_up: Optional[_LightPowerUp] = None
    id_v1: Optional[str] = None


    def to_put(self) -> dict:
        """Converts self into a JSON-style dict that is a valid PUT request to /resource/light"""

        return json.dumps({
            'on': {
                'on': self.on.on
            }
        })
