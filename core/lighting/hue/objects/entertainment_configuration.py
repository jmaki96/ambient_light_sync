from dataclasses import dataclass
from typing import Optional, List

from dataclasses_json import DataClassJsonMixin

from core.lighting.hue.enums import EntertainmentConfigurationType, EntertainmentConfigurationStatus, StreamProxyMode, ResourceType
from core.lighting.hue.objects.position import Position
from core.lighting.hue.objects.resource import Resource

@dataclass
class _ECMetadata(DataClassJsonMixin):
    name: str


@dataclass
class _ECStreamProxy(DataClassJsonMixin):
    mode: StreamProxyMode
    node: Resource


@dataclass
class EntertainmentChannelSegment(DataClassJsonMixin):
    index: int
    service: Resource


@dataclass
class EntertainmentChannel(DataClassJsonMixin):
    channel_id: int
    position: Position
    members: List[EntertainmentChannelSegment]


@dataclass
class ServiceLocation(DataClassJsonMixin):
    service: Resource
    positions: List[Position]
    equalization_factor: float # [-1.0, 1.0]

    position: Optional[Position] = None


@dataclass
class _ECLocations(DataClassJsonMixin):
    service_locations: List[ServiceLocation]

@dataclass
class EntertainmentConfiguration(DataClassJsonMixin):
    """An EntertainmentConfiguration defines a configuration of resources as used by the Hue Entertainment API. 
        It is key for synchronized, streaming applications."""
    
    id: str
    metadata: _ECMetadata
    # name was deprecated and is now stored on metadata
    configuration_type: EntertainmentConfigurationType
    status: EntertainmentConfigurationStatus
    stream_proxy: _ECStreamProxy
    channels: List[EntertainmentChannel]
    locations: _ECLocations

    active_streamer: Optional[Resource] = None
    id_v1: Optional[str] = None
    # light_services is deprecated in favor of locations
    type: Optional[ResourceType] = ResourceType.ENTERTAINMENT_CONFIGURATION