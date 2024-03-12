from abc import abstractmethod
from Animal import Animal

class Carnivoro(Animal):
    
    @abstractmethod
    def cazar(self):
        pass