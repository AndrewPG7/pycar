from factory.mock_car import create_car

car = create_car()

print(f"START {car.name} CAR")

car.light_control.head_lights_on()
car.drive_control.set_speed(1.0)
car.light_control.blink_left()
car.drive_control.turn_left()
car.drive_control.turn_reset()
car.drive_control.set_speed(0.5)
car.light_control.blink_right()
car.drive_control.set_speed(0.3)
car.drive_control.turn_right()
car.drive_control.turn_reset()
car.drive_control.stop()
car.light_control.head_lights_off()

print("CAR END")