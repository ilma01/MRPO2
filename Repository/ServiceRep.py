from Repository import Repos

class Services(Repos.FakeRepos):
    def __init__(self):
        self.services = []

    def add(self, service):
        self.services.append(service)

    def remove(self, service):
        if self.services:
            for s in self.services:
                if s.id == service.id:
                    self.services.remove(s)

    def get_all(self):
        return self.services

    def get(self, id):
        if self.services:
            for s in self.services:
                if s.id == id:
                    return s