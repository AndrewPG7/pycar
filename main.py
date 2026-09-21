import time

from factory.mock_car import create_car

#from factory.raspberrypi_car import create_car, destroy_car

car = create_car()

print(f"START {car.name} CAR")


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

#destroy_car(car)

print("CAR END")