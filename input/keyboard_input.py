import keyboard

from input.car_commands import CarCommands
from input.input import Input


class KeyboardInput(Input):
    def __init__(self):
        self.speed = 0.0
    
    def get_command(self):
        if keyboard.is_pressed("up"):
            self.speed = 1.0
        elif keyboard.is_pressed("down"):
            self.speed = -1.0
        else:
            self.speed = 0.0
            
        return CarCommands(speed=self.speed)