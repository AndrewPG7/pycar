from gpiozero import LED

from components.light import Light


class GPIOLight(Light):
    def __init__(self, name, pin):
        self.name = name
        self._led = LED(pin)

    def on(self):
        print(f"{self.name} ON")
        self._led.on()

    def off(self):
        print(f"{self.name} OFF")
        self._led.off()

    def blink(self):
        print(f"{self.name} BLINK")
        self._led.blink()
