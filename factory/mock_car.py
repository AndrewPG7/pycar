from car.car import Car
from control.drive_control import DriveControl
from control.light_control import LightControl
from hardware.mock.light import MockLight
from hardware.mock.motor import MockMotor
from hardware.mock.steer import MockSteer


def create_car():

    motor_right = MockMotor("Motor Right")
    motor_left = MockMotor("Motor Left")

    steer = MockSteer()

    drive_control = DriveControl(motor_right, motor_left, steer)

    head_light = MockLight("Head Light")
    blinker_right = MockLight("Blinker Right")
    blinker_left = MockLight("Blinker Left")

    light_control = LightControl(head_light, blinker_right, blinker_left)

    return Car("MOCK", drive_control, light_control)