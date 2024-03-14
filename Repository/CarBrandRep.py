from Repository import Repos

class CarBrandRepos(Repos.FakeRepos):
    def __init__(self):
        self.brands = []

    def add(self, brand):
        self.brands.append(brand)

    def remove(self, brand):
        if self.brands:
            for b in self.brands:
                if b.name == brand.name:
                    self.brands.remove(b)

    def get_all(self):
        return self.brands

    def get(self, name):
        if self.brands:
            for b in self.brands:
                if b.name == name:
                    return b