from abc import ABC, abstractmethod

class Repository(ABC):

    @abstractmethod
    def add(self, text):
        pass

    @abstractmethod
    def get_all(self):
        pass