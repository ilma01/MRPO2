from datetime import datetime
from typing import List
import CarBrand
from dataclasses import dataclass, field
from Consumable import Consumable

@dataclass(frozen=True)
class CarModel:
    name: str
    brand: CarBrand
    year: datetime.year = None
    body_type: str = None
    engine_volume: float = None
    recommended_parts: List[Consumable] = field(default_factory=list)