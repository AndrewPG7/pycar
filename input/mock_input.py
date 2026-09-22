from itertools import cycle

from input.car_commands import CarCommands
from input.input import Input


class MockInput(Input):
    def __init__(self, commands):
        print("MockInput init")
        self.commands = iter(commands)
        self.commands_iterator = cycle(self.commands)

    def get_command(self) -> CarCommands | None:
        try:
            return next(self.commands)
        except StopIteration:
            return None