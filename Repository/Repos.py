from abc import ABC, abstractmethod

class FakeRepos(ABC):
    def __init__(self, session):
        self.session = session

    @abstractmethod
    def add(self, item):
        pass

    @abstractmethod
    def remove(self, item):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get(self):
        pass