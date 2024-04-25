from datetime import datetime
from dataclasses import dataclass

@dataclass(frozen=True)
class CarBrand:
    name: str
    country: str = None
    founding_year: datetime.year = None
