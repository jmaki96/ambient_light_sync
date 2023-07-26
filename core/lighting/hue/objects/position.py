from dataclasses_json import DataClassJsonMixin


from dataclasses import dataclass


@dataclass
class Position(DataClassJsonMixin):
    x: float # [-1.0, 1.0]
    y: float # [-1.0, 1.0]
    z: float # [-1.0, 1.0]