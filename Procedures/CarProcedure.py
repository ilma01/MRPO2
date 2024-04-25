import datetime
import warnings

from Repository import Repos
from Models.Car import Car
from Models.CarModel import CarModel
import business_rules


class CarProcedure:
    def __init__(self, car_repository: Repos):
        self.car_repository = car_repository

    def get_car(self, vin: str) -> Car:
        return self.car_repository.get(vin)

    def add_car(self, model: CarModel, mileage: int = 0, year: int = datetime.date.today().year, vin: str = None):
        if vin:
            if not vin.isalnum():
                raise ValueError("VIN должен состоять только из букв и цифр")
        if self.get_car(vin) and vin:
            warnings.warn("Автомобиль с указанным VIN уже существует", UserWarning)
        elif not model:
            raise ValueError("Такой модели не существует")
        else:
            car = Car(model, mileage, year, vin)
            if business_rules.mileage_non_negative(car):
                self.car_repository.add(car)

    def update_car_mileage(self, new_mileage: int, vin: str = None, car: Car = None):
        if new_mileage < 0:
            raise ValueError('Новый пробег не должен быть отрицательным')
        if vin:
            car = self.get_car(vin)
        if car:
            car.mileage = new_mileage
            self.car_repository.update(car)
        else:
            warnings.warn("Автомобиль не выбран", UserWarning)

    def remove_car(self, vin: str = None, car: Car = None):
        if vin:
            car = self.get_car(vin)
        if car:
            self.car_repository.remove(car)
        else:
            warnings.warn("Автомобиль не выбран", UserWarning)

    def get_all_cars(self) -> list[Car]:
        return self.car_repository.get_all()