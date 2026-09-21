from dataclasses import dataclass


@dataclass
class CarCommands:
    speed: float = 0.0
    steer: float = 0.0

    blinker_r: bool = False
    blinker_l: bool = False
    headlight: bool = False