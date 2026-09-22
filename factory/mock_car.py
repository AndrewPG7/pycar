from car.car import Car
from control.drive_control import DriveControl
from control.light_control import LightControl
from hardware.mock.light import MockLight
from hardware.mock.motor import MockMotor
from hardware.mock.steer import MockSteer
from input.car_commands import CarCommands
from input.keyboard_input import KeyboardInput
from input.mock_input import MockInput


def create_car():

    motor_right = MockMotor("Motor Right")
    motor_left = MockMotor("Motor Left")

    steer = MockSteer()

    drive_control = DriveControl(motor_right, motor_left, steer)

    head_light = MockLight("Head Light")
    blinker_right = MockLight("Blinker Right")
    blinker_left = MockLight("Blinker Left")

    light_control = LightControl(head_light, blinker_right, blinker_left)

    """
    input = MockInput(
        [
            CarCommands(speed=0.0),
            CarCommands(speed=0.3),
            CarCommands(speed=0.5),
            CarCommands(speed=0.8),
            CarCommands(speed=1.0),
            CarCommands(speed=0.0),
            CarCommands(speed=-0.3),
            CarCommands(speed=-0.5),
            CarCommands(speed=-0.8),
            CarCommands(speed=-1.0),
            CarCommands(speed=0.0),
        ]
    )
    """

    input = KeyboardInput()

    return Car("MOCK CAR", drive_control, light_control, input)

def destroy_car(car):
    print(f"DESTROY {car.name}")