from Repository import Repos

class CarBrandRepos(Repos.FakeRepos):
    def __init__(self):
        self.brands = []

    def get(self, name):
        for brand in self.brands:
            if brand.name == name:
                return brand
        return None

    def add(self, brand):
        self.brands.append(brand)

    def remove(self, brand):
        if brand in self.brands:
            self.brands.remove(brand)

    def update(self, brand):
        existing_brand = self.get(brand.name)
        if existing_brand:
            self.brands.remove(existing_brand)
            self.brands.append(brand)

    def get_all(self):
        return self.brands