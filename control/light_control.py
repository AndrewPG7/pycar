import time

from components.light import Light

BLINK_INTERVAL = 0.5

class LightControl:
    def __init__(self, head_lights, blink_right, blink_left):
        self.head_lights = head_lights
        
        self.blinker_right = blink_right
        self.blinker_left = blink_left
        
    def head_lights_on(self):
        self.head_lights.on()
        
    def head_lights_off(self):
        self.head_lights.off()

    def _blink(self, blinker, blinkc_times):
        for _ in range(blinkc_times):
            blinker.on()
            time.sleep(BLINK_INTERVAL)
            
            blinker.off()
            time.sleep(BLINK_INTERVAL)

    def blink_right(self, blink_times=3):
        self._blink(self.blinker_right, blink_times)

    def blink_left(self, blink_times=3):
        self._blink(self.blinker_left, blink_times)