from control.drive_control import DriveControl
from control.light_control import LightControl


class Car():
    def __init__(self, name, drive_control, light_control):
        self.name = name
        self.drive_control = drive_control
        self.light_control = light_control

"""
    def set_speed(self, speed):
        self.drive_control.set_speed(speed)

    def stop(self):
        self.drive_control.stop()

    def turn_right(self):
        self.drive_control.turn_right()

    def turn_left(self):
        self.drive_control.turn_left()

    def turn_reset(self):
        self.drive_control.turn_reset()

    def head_lights_on(self):
        self.light_control.head_lights_on()

    def head_lights_off(self):
        self.light_control.head_lights_off()

    def blink_right(self):
        self.light_control.blink_right()

    def blink_left(self):
        self.light_control.blink_left()
"""