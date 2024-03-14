import datetime

import CarBrand
class CarModel:
    def __init__(self, name: str, brand: CarBrand.CarBrand, year: datetime.datetime.year = None, body_type: str = None, engine_volume: float = None):
        self.name = name
        self.year = year
        self.body_type = body_type
        self.engine_volume = engine_volume
        self.brand = brand
        self.brand.models.append(self)
        self.cars = []

    def get_info(self):
        return {
            "brand": self.brand.get_info(),
            "name": self.name,
            "year": self.year,
            "body_type": self.body_type,
            "engine_capacity": self.engine_volume
        }