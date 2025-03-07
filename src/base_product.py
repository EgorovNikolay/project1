from abc import ABC, abstractmethod

class BaseProduct(ABC):
    @abstractmethod
    def __init__(self, name, description, quantity):
        self.name = name
        self.description = description
        self.quantity = quantity

    def __str__(self):
        pass
