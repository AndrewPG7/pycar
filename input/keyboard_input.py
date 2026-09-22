import keyboard

from input.car_commands import CarCommands
from input.input import Input


class KeyboardInput(Input):
    
    def get_command(self):
        speed = 0.0
        if keyboard.is_pressed("up"):
            speed = 1.0
        elif keyboard.is_pressed("down"):
            speed = -1.0
        return CarCommands(speed=speed)