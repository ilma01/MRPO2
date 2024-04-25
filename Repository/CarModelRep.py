from Repository import Repos

class CarModelRepos(Repos.FakeRepos):
    def __init__(self):
        self.models = []

    def get(self, name):
        for model in self.models:
            if model.name == name:
                return model
        return None

    def get_by_name_and_brand(self, name, brand):
        for model in self.models:
            if model.name == name and model.brand == brand:
                return model
        return None
    def add(self, model):
        self.models.append(model)

    def remove(self, model):
        if model in self.models:
            self.models.remove(model)

    def update(self, model):
        existing_model = self.get_by_name_and_brand(model.name, model.brand)
        if existing_model:
            self.models.remove(existing_model)
            self.models.append(model)

    def get_all(self):
        return self.models