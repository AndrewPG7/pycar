from abc import ABC, abstractmethod


class Steer(ABC):
        
    @abstractmethod
    def reset(self):
        pass
        
    @abstractmethod
    def right(self):
        pass
        
    @abstractmethod
    def left(self):
        pass