from dataclasses import dataclass

@dataclass(frozen=True)
class Consumable:
    name: str
    manufacturer: str
    cost: float