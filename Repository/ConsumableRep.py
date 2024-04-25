from Repository import Repos

class ConsumableRepos(Repos.FakeRepos):
    def __init__(self):
        self.consumables = []

    def get(self, name):
        for consumable in self.consumables:
            if consumable.name == name:
                return consumable
        return None

    def add(self, consumable):
        self.consumables.append(consumable)

    def remove(self, consumable):
        if consumable in self.consumables:
            self.consumables.remove(consumable)

    def update(self, consumable):
        existing_consumable = self.get(consumable.name)
        if existing_consumable:
            self.consumables.remove(existing_consumable)
            self.consumables.append(consumable)

    def get_all(self):
        return self.consumables
