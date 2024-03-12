from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def comer(self):
        pass

    @abstractmethod
    def dormir(self):
        pass

    @abstractmethod
    def respirar(self):
        pass