from car.car import Car
from control.drive_control import DriveControl
from control.light_control import LightControl
from hardware.raspberrypi.light import GPIOLight
from hardware.raspberrypi.motor import GPIOMotor

#from hardware.raspberrypi.steer import GPIOSteer


HEADLIGHT_PIN = 24
BLINKER_R_PIN = 25
BLINKER_L_PIN =  23
                        # L293D PIN:
MOTOR_R_IN_1_PIN =  5   # 2
MOTOR_R_IN_2_PIN =  6   # 7
MOTOR_R_EN_PIN =    26  # 1
MOTOR_L_IN_1_PIN =  24  # 15
MOTOR_L_IN_2_PIN =  25  # 10
MOTOR_L_EN_PIN =    23  # 9


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

    return Car(
        "GPIO",
        drive_control
    )

def destroy_car(car):
    car.drive_control.motor_right.destroy()
    car.drive_control.motor_left.destroy()