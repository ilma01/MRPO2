import warnings
from datetime import datetime
from typing import List
from Repository import Repos
from Models.CarModel import CarModel
from Models.CarBrand import CarBrand
from Models.Consumable import Consumable


class CarModelProcedure:
    def __init__(self, car_model_repository: Repos):
        self.car_model_repository = car_model_repository

    def get_model(self, name: str) -> CarModel:
        return self.car_model_repository.get(name)

    def add_model(self, name: str, brand: CarBrand, year: int = datetime.now().year,
                  body_type: str = None, engine_volume: float = None,
                  recommended_parts: List[Consumable] = []):
        if not brand:
            raise ValueError("Такого бренда не существует")
        existing_model = self.car_model_repository.get(name)
        if existing_model:
            warnings.warn("Модель автомобиля с указанным именем уже существует", UserWarning)
        else:
            car_model = CarModel(name, brand, year, body_type, engine_volume, recommended_parts)
            self.car_model_repository.add(car_model)

    def update_model(self, name: str,
                     year: int = None, body_type: str = None, engine_volume: float = None,
                     recommended_parts: List[Consumable] = []):
        car_model = self.get_model(name)
        if car_model:
            updated_model = CarModel(car_model.name,
                                     car_model.brand,
                                     year if year else car_model.year,
                                     body_type if body_type else car_model.body_type,
                                     engine_volume if engine_volume else car_model.engine_volume,
                                     recommended_parts if recommended_parts else car_model.recommended_parts)
            self.car_model_repository.update(updated_model)
        else:
            warnings.warn("Модель автомобиля с указанным именем не найдена", UserWarning)

    def remove_model(self, name: str):
        car_model = self.get_model(name)
        if car_model:
            self.car_model_repository.remove(car_model)
        else:
            warnings.warn("Модель автомобиля с указанным именем не найдена", UserWarning)

    def get_all_models(self) -> List[CarModel]:
        return self.car_model_repository.get_all()