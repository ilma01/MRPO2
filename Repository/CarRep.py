from Repository import Repos

class CarRepos(Repos.FakeRepos):
    def __init__(self):
        self.cars = []

    def get(self, vin):
        if self.cars:
            for c in self.cars:
                if c.vin == vin:
                    return c
            return None

    def add(self, car):
        self.cars.append(car)

    def remove(self, car):
        if car in self.cars:
            self.cars.remove(car)

    def update(self, car):
        c = self.get(car.vin)
        if c:
            self.cars.remove(c)
            self.cars.append(car)

    def get_all(self):
        return self.cars