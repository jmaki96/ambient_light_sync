from dataclasses import dataclass
from typing import List, Optional

from dataclasses_json import DataClassJsonMixin

from core.lighting.hue.enums import Archetype, ResourceType
from core.lighting.hue.objects.resource import Resource


@dataclass
class _ProductData(DataClassJsonMixin):
    """ Only exists as part of a DeviceGet and should not be instantiated on its own."""
    model_id: str
    manufacturer_name: str
    product_name: str
    product_archetype: Archetype
    certified: bool
    software_version: str
    hardware_platform_type: Optional[str] = None


@dataclass
class _DeviceMetadata(DataClassJsonMixin):
    """ Only exists as part of a DeviceGet and should not be instantiated on its own."""
    name: str
    archetype: Archetype


@dataclass
class Device(DataClassJsonMixin):
    """An instance of a Hue DeviceGet as returned by the /resource/device endpoint.
    
    See: https://developers.meethue.com/develop/hue-api-v2/api-reference/#resource_device_get"""

    type: ResourceType
    id: str
    product_data: _ProductData
    metadata: _DeviceMetadata
    services: List[Resource]
    id_v1: Optional[str] = None

    def get_resources_by_type(self, resource_type: ResourceType) -> List[Resource]:
        """Returns all resources of this device by the rtype.

        Args:
            resource_type (ResourceType): the rtype or Resource Type of the services to get

        Returns:
            List[Resource]: All resources of specified type.
        """

        return [resource for resource in self.services if resource.rtype == resource_type]
