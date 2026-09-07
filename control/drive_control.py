from components.motor import Motor
from components.steer import Steer


class DriveControl:
    def __init__(self, motor_right, motor_left, steer):
        self.motor_right = motor_right
        self.motor_left = motor_left
        
        self.steer = steer
        
    def set_speed(self, speed):
        self.motor_right.set_speed(speed)
        self.motor_left.set_speed(speed)
        
    def stop(self):
        self.motor_right.stop()
        self.motor_left.stop()
    
    def turn_right(self):
        self.steer.right()

    def turn_left(self):
        self.steer.left()

    def turn_reset(self):
        self.steer.reset()