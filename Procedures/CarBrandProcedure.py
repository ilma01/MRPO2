import warnings

from Models.CarBrand import CarBrand
from Repository import Repos

class CarBrandProcedure:
    def __init__(self, brand_repository: Repos):
        self.brand_repository = brand_repository

    def get_brand(self, name: str) -> CarBrand:
        return self.brand_repository.get(name)

    def add_brand(self, name: str, country: str = None, founding_year: int = None):
        if self.get_brand(name):
            warnings.warn("Марка автомобиля с указанным именем уже существует", UserWarning)
        else:
            brand = CarBrand(name, country, founding_year)
            self.brand_repository.add(brand)

    def update_brand(self, name: str, country: str = None, founding_year: int = None):
        brand = self.get_brand(name)
        if brand:
            updated_brand = CarBrand(brand.name,
                                     country if country else brand.country,
                                     founding_year if founding_year else brand.founding_year)
            self.brand_repository.update(updated_brand)
        else:
            warnings.warn("Марка автомобиля с указанным именем не найдена", UserWarning)

    def remove_brand(self, name: str):
        brand = self.get_brand(name)
        if brand:
            self.brand_repository.remove(brand)
        else:
            warnings.warn("Марка автомобиля с указанным именем не найдена", UserWarning)

    def get_all_brands(self) -> list[CarBrand]:
        return self.brand_repository.get_all()
