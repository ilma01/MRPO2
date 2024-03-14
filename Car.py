import datetime

import CarModel
class Car:
    def __init__(self, model: CarModel.CarModel, mileage: int, year: datetime.datetime.year, vin: str):
        self.mileage = mileage
        self.year = year
        self.vin = vin
        self.model = model
        self.model.cars.append(self)
        self.services = []

    def get_info(self):
        return {
            "model": self.model.get_info(),
            "mileage": self.mileage,
            "year": self.year,
            "vin": self.vin
        }
