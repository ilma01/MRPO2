import warnings
from datetime import datetime
from typing import List
from Repository import Repos
from Models.Service import Service
from Models.Car import Car
from Models.Consumable import Consumable
from business_rules import can_go_to_service, used_recommended_consumables

class ServiceProcedure:
    def __init__(self, service_repository: Repos):
        self.service_repository = service_repository
        self.next_id = 1

    def get_service(self, service_id: int) -> Service:
        return self.service_repository.get(service_id)

    def get_all_services(self) -> List[Service]:
        return self.service_repository.get_all()

    def add_service(self, car: Car, cost: float, date: datetime = datetime.now(), service_type: str = 'Плановое', tasks: str = None, consumables: List[Consumable] = None):
        if can_go_to_service(car):
            service = Service(self.next_id, date, service_type, cost, car, tasks, consumables)
            self.service_repository.add(service)
            self.next_id += 1
            if not used_recommended_consumables(service):
                warnings.warn("При обслуживании автомобиля должны использоваться рекомендованные производителем расходные материалы", UserWarning)
        else:
            warnings.warn("Не выполнены условия для проведения обслуживания автомобиля", UserWarning)

    def update_service(self, service_id: int, new_service_id: int = None, date: datetime = None, service_type: str = None, cost: float = None, car: Car = None, tasks: str = None, consumables: List[Consumable] = None):
        service = self.get_service(service_id)
        if service:
            updated_service = Service(new_service_id if new_service_id else service.id,
                                      date if date else service.date,
                                      service_type if service_type else service.service_type,
                                      cost if cost else service.cost,
                                      car if car else service.car,
                                      tasks if tasks else service.tasks,
                                      consumables if consumables else service.consumables)
            self.service_repository.update(updated_service)
        else:
            warnings.warn("Услуга с указанным идентификатором не найдена", UserWarning)

    def remove_service(self, service_id: int):
        service = self.get_service(service_id)
        if service:
            self.service_repository.remove(service)
        else:
            warnings.warn("Услуга с указанным идентификатором не найдена", UserWarning)