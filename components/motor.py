from abc import ABC, abstractmethod


class Motor(ABC):

    @abstractmethod        
    def set_speed(self, speed):
        pass
        
    @abstractmethod
    def stop(self):
        pass