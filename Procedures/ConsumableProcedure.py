import warnings

from Repository import Repos
from Models.Consumable import Consumable

class ConsumableProcedure:
    def __init__(self, consumable_repository: Repos):
        self.consumable_repository = consumable_repository

    def get_consumable(self, name: str) -> Consumable:
        return self.consumable_repository.get(name)

    def add_consumable(self, name: str, manufacturer: str, cost: float):
        existing_consumables = self.consumable_repository.get_all()
        _exists = False
        for consumable in existing_consumables:
            if consumable.name == name and consumable.manufacturer == manufacturer:
                warnings.warn("Расходный материал с таким именем у этого производителя уже существует", UserWarning)
                _exists = True
        if not _exists:
            consumable = Consumable(name, manufacturer, cost)
            self.consumable_repository.add(consumable)

    def update_consumable(self, name: str, manufacturer: str = None, cost: float = None):
        consumable = self.get_consumable(name)
        if consumable:
            updated_consumable = Consumable(name,
                                             manufacturer if manufacturer else consumable.manufacturer,
                                             cost if cost else consumable.cost)
            self.consumable_repository.update(updated_consumable)
        else:
            warnings.warn("Расходный материал с указанным именем не найден", UserWarning)

    def remove_consumable(self, name: str):
        consumable = self.get_consumable(name)
        if consumable:
            self.consumable_repository.remove(consumable)
        else:
            warnings.warn("Расходный материал с указанным именем не найден", UserWarning)

    def get_all_consumables(self):
        return self.consumable_repository.get_all()
