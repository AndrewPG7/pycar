from abc import ABC, abstractmethod

from input.car_commands import CarCommands


class Input(ABC):

    @abstractmethod
    def get_command(self) -> CarCommands:
        pass