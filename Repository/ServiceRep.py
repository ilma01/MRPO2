from Repository import Repos
from Models.Service import Service
from typing import List

class Services(Repos.FakeRepos):
    def __init__(self):
        self.services = []

    def get(self, service_id: int) -> Service:
        for service in self.services:
            if service.id == service_id:
                return service
        return None

    def add(self, service: Service):
        self.services.append(service)

    def remove(self, service: Service):
        if service in self.services:
            self.services.remove(service)

    def update(self, service: Service):
        existing_service = self.get(service.id)
        if existing_service:
            self.services.remove(existing_service)
            self.services.append(service)

    def get_all(self) -> List[Service]:
        return self.services