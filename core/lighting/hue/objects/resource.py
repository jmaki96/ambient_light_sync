from dataclasses import dataclass

from dataclasses_json import DataClassJsonMixin

from core.lighting.hue.enums import ResourceType


@dataclass
class Resource(DataClassJsonMixin):
    rid: str
    rtype: ResourceType