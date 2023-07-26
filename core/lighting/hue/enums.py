from enum import Enum


class Archetype(Enum):
    BOLLARD='bollard'
    BRIDGE_V2='bridge_v2'
    CANDLE_BULB='candle_bulb'
    CEILING_HORIZONTAL='ceiling_horizontal'
    CEILING_ROUND='ceiling_round'
    CEILING_SQUARE='ceiling_square'
    CEILING_TUBE='ceiling_tube'
    CHRISTMAS_TREE='christmas_tree'
    CLASSIC_BULB='classic_bulb'
    DOUBLE_SPOT='double_spot'
    EDISON_BULB='edison_bulb'
    ELLIPSE_BULB='ellipse_bulb'
    FLEXIBLE_LAMP='flexible_lamp'
    FLOOD_BULB='flood_bulb'
    FLOOR_LANTERN='floor_lantern'
    FLOOR_SHADE='floor_shade'
    GROUND_SPOT='ground_spot'
    HUE_BLOOM='hue_bloom'
    HUE_CENTRIS='hue_centris'
    HUE_GO='hue_go'
    HUE_IRIS='hue_iris'
    HUE_LIGHTSTRIP='hue_lightstrip'
    HUE_LIGHTSTRIP_PC='hue_lightstrip_pc'
    HUE_LIGHTSTRIP_TV='hue_lightstrip_tv'
    HUE_PLAY='hue_play'
    HUE_SIGNE='hue_signe'
    HUE_TUBE='hue_tube'
    LARGE_GLOBE_BULB='large_globe_bulb'
    LUSTER_BULB='luster_bulb'
    PENDANT_LONG='pendant_long'
    PENDANT_ROUND='pendant_round'
    PENDANT_SPOT='pendant_spot'
    PLUG='plug'
    RECESSED_CEILING='recessed_ceiling'
    RECESSED_FLOOR='recessed_floor'
    SINGLE_SPOT='single_spot'
    SMALL_GLOBE_BULB='small_globe_bulb'
    SPOT_BULB='spot_bulb'
    STRING_LIGHT='string_light'
    SULTAN_BULB='sultan_bulb'
    TABLE_SHADE='table_shade'
    TABLE_WASH='table_wash'
    TRIANGLE_BULB='triangle_bulb'
    UNKNOWN_ARCHETYPE='unknown_archetype'
    VINTAGE_BULB='vintage_bulb'
    VINTAGE_CANDLE_BULB='vintage_candle_bulb'
    WALL_LANTERN='wall_lantern'
    WALL_SHADE='wall_shade'
    WALL_SPOT='wall_spot'
    WALL_WASHER='wall_washer'


class EntertainmentConfigurationType(Enum):
    SCREEN='screen'
    MONITOR='monitor'
    MUSIC='music'
    THREEDSPACE='3dspace'
    OTHER='other'


class EntertainmentConfigurationStatus(Enum):
    ACTIVE='active'
    INACTIVE='inactive'


class StreamProxyMode(Enum):
    AUTO='auto'
    MANUAL='manual'


class SupportedDynamicStatus(Enum):
    DYNAMIC_PALETTE='dynamic_palette'
    NONE='none'


class GamutType(Enum):
    A='A'
    B='B'
    C='C'
    OTHER='other'


class SupportedEffect(Enum):
    SPARKLE='sparkle'
    FIRE='fire'
    CANDLE='candle'
    PRISM='prism'
    NO_EFFECT='no_effect'


class SupportedTimedEffect(Enum):
    SUNRISE='sunrise'
    NO_EFFECT='no_effect'


class PowerUpColorMode(Enum):
    COLOR_TEMPERATURE='color_temperature'
    COLOR='color'
    PREVIOUS='previous'


class PowerUpDimmingMode(Enum):
    DIMMING='dimming'
    PREVIOUS='previous'


class PowerUpOnMode(Enum):
    ON='on'
    TOGGLE='toggle'
    PREVIOUS='previous'


class PowerUpPreset(Enum):
    CUSTOM='custom'
    LAST_ON_STATE='last_on_state'
    POWERFAIL='powerfail'
    SAFETY='safety'


class SupportedGradientMode(Enum):
    INTERPOLATED_PALETTE='interpolated_palette'
    INTERPOLATED_PALETTE_MIRRORED='interpolated_palette_mirrored'
    RANDOM_PIXELATED='random_pixelated'


class LightMode(Enum):
    NORMAL='normal'
    STREAMING='streaming'


class ResourceType(Enum):
    AUTH_V1='auth_v1'
    BEHAVIOR_INSTANCE='behavior_instance'
    BEHAVIOR_SCRIPT='behavior_script'
    BRIDGE='bridge'
    BRIDGE_HOME='bridge_home'
    BUTTON='button'
    DEVICE='device'
    DEVICE_POWER='device_power'
    ENTERTAINMENT='entertainment'
    ENTERTAINMENT_CONFIGURATION='entertainment_configuration'
    GEOFENCE='geofence'
    GEOFENCE_CLIENT='geofence_client'
    GEOLOCATION='geolocation'
    GROUPED_LIGHT='grouped_light'
    HOMEKIT='homekit'
    LIGHT='light'
    LIGHT_LEVEL='light_level'
    MATTER='matter'
    MATTER_FABRIC='matter_fabric'
    MOTION='motion'
    PUBLIC_IMAGE='public_image'
    RELATIVE_ROTARY='relative_rotary'
    ROOM='room'
    SCENE='scene'
    SMART_SCENE='smart_scene'
    TEMPERATURE='temperature'
    ZGP_CONNECTIVITY='zgp_connectivity'
    ZIGBEE_BRIDGE_CONNECTIVITY='zigbee_bridge_connectivity'
    ZIGBEE_CONNECTIVITY='zigbee_connectivity'
    ZIGBEE_DEVICE_DISCOVERY='zigbee_device_discovery'
    ZONE='zone'


class SignalStatus(Enum):
    NO_SIGNAL='no_signal'
    ON_OFF='on_off'
