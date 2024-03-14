from Repository import Repos

class CarModelRepos(Repos.FakeRepos):
    def __init__(self):
        self.models = []

    def add(self, model):
        self.models.append(model)

    def remove(self, model):
        if self.models:
            for m in self.models:
                if m.name == model.name:
                    self.models.remove(m)

    def get_all(self):
        return self.models

    def get(self, name):
        if self.models:
            for m in self.models:
                if m.name == name:
                    return m