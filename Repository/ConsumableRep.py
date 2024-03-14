from Repository import Repos

class Consumables(Repos.FakeRepos):
    def __init__(self):
        self.consumables = []

    def add(self, consumable):
        self.consumables.append(consumable)

    def remove(self, consumable):
        if self.consumables:
            for c in self.consumables:
                if c.name == consumable.name:
                    self.consumables.remove(c)

    def get_all(self):
        return self.consumables

    def get(self, name):
        if self.consumables:
            for c in self.consumables:
                if c.name == name:
                    return c