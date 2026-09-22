import pygame

from input.car_commands import CarCommands
from input.input import Input


class GamepadInput(Input):
    def __init__(self):
        pygame.init()
        pygame.joystick.init()

        if pygame.joystick.get_count() == 0:
            raise RuntimeError("No gamepad")
        
        self.joystick = pygame.joystick.Joystick(0)
        self.joystick.init()    
        print(f"Connected gamepad: {self.joystick.get_name()}")
        
    def get_command(self):
        pygame.event.pump()

        speed_forward = self._map_trigger_value(self.joystick.get_axis(0))  #TODO: get correct trigger axis
        speed_backward = self._map_trigger_value(self.joystick.get_axis(1)) #TODO: get correct trigger axis
        speed = speed_forward - speed_backward
        return CarCommands(speed=speed)
    
    def _map_trigger_value(self, value: float) -> float:
        return (value + 1) / 2