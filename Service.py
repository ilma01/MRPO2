import datetime
import Car

class Service:
    def __init__(self, id, date: datetime.datetime, service_type: str, mileage: int, cost: float, car: Car.Car, tasks: str = None):
        self.id = id
        self.date = date
        self.service_type = service_type
        self.mileage = mileage
        self.cost = cost
        self.tasks = tasks
        self.car = car

    def get_info(self):
        return {
            "car": self.car.get_info(),
            "date": self.date,
            "service_type": self.service_type,
            "mileage": self.mileage,
            "cost": self.cost,
            "tasks": self.tasks
        }