from car.car import Car
from control.drive_control import DriveControl
from control.light_control import LightControl
from hardware.raspberrypi.light import GPIOLight
from hardware.raspberrypi.motor import GPIOMotor
from input.car_commands import CarCommands
from input.mock_input import MockInput

#from hardware.raspberrypi.steer import GPIOSteer


HEADLIGHT_PIN = 24
BLINKER_R_PIN = 25
BLINKER_L_PIN = 23
                        # L293D PIN:
MOTOR_R_IN_1_PIN =  23   # 2
MOTOR_R_IN_2_PIN =  24  # 7
MOTOR_R_EN_PIN =    18  # 1
MOTOR_L_IN_1_PIN =  16  # 15
MOTOR_L_IN_2_PIN =  20  # 10
MOTOR_L_EN_PIN =    12  # 9


def create_car():
    motor_right = GPIOMotor(
        "Motor Right",
        MOTOR_R_IN_1_PIN,
        MOTOR_R_IN_2_PIN,
        MOTOR_R_EN_PIN
    )
    motor_left = GPIOMotor(
        "Motor Left",
        MOTOR_L_IN_1_PIN,
        MOTOR_L_IN_2_PIN,
        MOTOR_L_EN_PIN
    )

    drive_control = DriveControl(motor_right, motor_left)

    """
    head_light = GPIOLight(
        "Headlight",
        HEADLIGHT_PIN
    )
    right_blinker = GPIOLight(
        "Right Blinker",
        BLINKER_R_PIN
    )
    left_blinker = GPIOLight(
        "Left Blinker",
        BLINKER_L_PIN
    )
    """

    #light_control = LightControl(head_light, right_blinker, left_blinker)

    input = MockInput(
        [
            CarCommands(speed=0.0),
            CarCommands(speed=0.3),
            CarCommands(speed=0.5),
            CarCommands(speed=0.8),
            CarCommands(speed=1.0),
            CarCommands(speed=0.0),
            CarCommands(speed=0.3),
            CarCommands(speed=0.5),
            CarCommands(speed=0.8),
            CarCommands(speed=1.0),
            CarCommands(speed=0.0),
        ]
    )

    return Car("GPIO CAR", drive_control, input=input)

def destroy_car(car):
    print(f"DESTROY {car.name}")
    car.drive_control.motor_right.destroy()
    car.drive_control.motor_left.destroy()