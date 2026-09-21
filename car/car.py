class Car:
    def __init__(self, name, drive_control=None, light_control=None, input=None):
        self.name = name
        self.drive_control = drive_control
        self.light_control = light_control
        self.input = input

    def update(self):
        command = self.input.get_command()

        if command is None:
            return False

        self.drive_control.set_speed(command.speed)
        """
        if command.headlight:
            self.light_control.head_lights_on()
        else:
            self.light_control.head_lights_off()

        if command.blinker_r:
            self.light_control.blink_right()

        if command.blinker_l:
            self.light_control.blink_left()
        """
        return True