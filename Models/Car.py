import datetime

from Models import CarModel
class Car:
    def __init__(self, model: CarModel.CarModel, mileage: int, year: datetime.datetime.year, vin: str, last_service_mileage = 0, last_service_date = datetime.datetime.now().date()):
        self.mileage = mileage
        self.year = year
        self.vin = vin
        self.model = model
        self.services = []
        self.last_service_mileage = last_service_mileage
        self.last_service_date = last_service_date
    def service_completed(self, mileage, service_date):
        self.last_service_mileage = mileage
        self.last_service_date = service_date
    def get_info(self):
        return {
            "model": self.model.name,
            "mileage": self.mileage,
            "year": self.year,
            "vin": self.vin
        }

    def __eq__(self, other):
        if not isinstance(other, Car):
            return False
        return (self.model == other.model and
                self.mileage == other.mileage and
                self.year == other.year and
                self.vin == other.vin)
