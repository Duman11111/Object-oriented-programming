from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def max_speed(self):
        pass