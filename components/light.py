from abc import ABC, abstractmethod


class Light(ABC):
        
    @abstractmethod
    def on(self):
        pass
        
    def off(self):
        pass