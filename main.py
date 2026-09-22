import sys
import time

from factory.mock_car import create_car, destroy_car

# from factory.raspberrypi_car import create_car, destroy_car


LOOP_TIME = 0.5


def main() -> int:
    car = None

    try:
        car = create_car()
        print(f"START {car.name}")

        while car.update():
            time.sleep(LOOP_TIME)

    except KeyboardInterrupt:
        print("\nInterrupt started")
    except Exception:
        print("\nERROR:")
        import traceback

        traceback.print_exc()
        return 1
    finally:
        if car is not None:
            try:
                destroy_car(car)
            except Exception:
                print("ERROR destroying car")
                import traceback

                traceback.print_exc()
        print("END CAR")
    return 0


if __name__ == "__main__":
    sys.exit(main())