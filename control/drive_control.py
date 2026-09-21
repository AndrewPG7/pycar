class DriveControl:
    def __init__(self, motor_right, motor_left, steer=None):
        self.motor_right = motor_right
        self.motor_left = motor_left

        self.steer = steer

    def set_speed(self, speed):
        self.motor_right.set_speed(speed)
        self.motor_left.set_speed(speed)

    # speed:        -1.0 Max Backwards, +1.0 Max Forwards
    # direction:    -1.0 Left, +1.0 Right
    def diferential_set_speed(self, speed, direction):
        motor_right_speed = speed - direction
        motor_left_speed = speed + direction

        self.motor_right.set_speed(max(-1, min(motor_right_speed)))
        self.motor_left.set_speed(max(-1, min(motor_left_speed)))

    def stop(self):
        self.motor_right.stop()
        self.motor_left.stop()

    def turn_right(self):
        self.steer.right()

    def turn_left(self):
        self.steer.left()

    def turn_reset(self):
        self.steer.reset()

