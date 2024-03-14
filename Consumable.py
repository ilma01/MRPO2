class Consumable:
    def __init__(self, name: str, manufacturer: str, cost: float):
        self.name = name
        self.manufacturer = manufacturer
        self.cost = cost

    def get_info(self):
        return {
            "name": self.name,
            "manufacturer": self.manufacturer,
            "cost": self.cost
        }