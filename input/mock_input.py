from input.car_commands import CarCommands
from input.input import Input


class MockInput(Input):

    def __init__(self, commands):
        print("MockInput init")
        self.commands = iter(commands)

    def get_command(self) -> CarCommands | None:
        return CarCommands(speed=1.0)

    """
    def get_command(self) -> CarCommands | None:
        try:
            return next(self.commands)
        except StopIteration:
            return None
    """