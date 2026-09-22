import sys
import time

from factory.mock_car import create_car, destroy_car

# from factory.raspberrypi_car import create_car, destroy_car

car = create_car()

try:
    print(f"START {car.name}")

    while car.update():
        time.sleep(3)

except KeyboardInterrupt:
    sys.exit()
finally:
    if car is not None:
        destroy_car(car)
    print("END CAR")