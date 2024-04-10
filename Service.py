import datetime
import Car
from Consumable import Consumable

class Service:
    def __init__(self, id, date: datetime.datetime, service_type: str, cost: float, car: Car.Car, tasks: str = None, consumables: list[Consumable] = None):
        self.id = id
        self.car = car
        self.date = date
        self.service_type = service_type
        self.mileage = car.mileage
        self.cost = cost
        self.tasks = tasks
        self.car.services.append(self)
        self.car.service_completed(self.mileage, self.date)
        if consumables:
            self.consumables = consumables
        else:
            self.consumables = []

    def get_info(self):
        return {
            "car": self.car.get_info(),
            "date": self.date,
            "service_type": self.service_type,
            "mileage": self.mileage,
            "cost": self.cost,
            "tasks": self.tasks
        }

    def __eq__(self, other):
        if not isinstance(other, Service):
            return False
        return (self.id == other.id and
                self.date == other.date and
                self.service_type == other.service_type and
                self.mileage == other.mileage and
                self.cost == other.cost and
                self.car == other.car and
                self.tasks == other.tasks and
                self.consumables == other.consumables)