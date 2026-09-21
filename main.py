import sys
import time

#from factory.mock_car import create_car
from factory.raspberrypi_car import create_car, destroy_car

try:
    car = create_car()

    print(f"START {car.name} CAR")

    while car.update():
        time.sleep(3)

    """
    car.light_control.head_lights_on()
    car.drive_control.set_speed(0.4)
    time.sleep(2.5)
    car.light_control.blink_left()
    car.drive_control.turn_left()
    car.drive_control.turn_reset()
    car.drive_control.set_speed(0.6)
    time.sleep(2.5)
    car.light_control.blink_right()
    car.drive_control.set_speed(0.8)
    time.sleep(2.5)
    car.drive_control.set_speed(1.0)
    time.sleep(2.5)
    car.drive_control.turn_right()
    car.drive_control.turn_reset()
    car.drive_control.stop()
    car.light_control.head_lights_off()
    """
except KeyboardInterrupt:
    sys.exit()
finally:
    print(f"END {car.name} CAR")
    destroy_car(car)