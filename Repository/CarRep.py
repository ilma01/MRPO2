from Repository import Repos

class CarRepos(Repos.FakeRepos):
    def __init__(self):
        self.cars = []

    def add(self, car):
        self.cars.append(car)

    def remove(self, car):
        if self.cars:
            for c in self.cars:
                if c.name == car.name:
                    self.cars.remove(c)

    def get_all(self):
        return self.cars

    def get(self, vin):
        if self.cars:
            for c in self.cars:
                if c.vin == vin:
                    return c