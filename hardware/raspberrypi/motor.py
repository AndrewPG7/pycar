from gpiozero import DigitalOutputDevice, PWMOutputDevice

from components.motor import Motor


class GPIOMotor(Motor):
    def __init__(self, name, in1, in2, en, pwm_frequency=1000):
        self.name = name
        self.in1 = in1
        self.in2 = in2
        self.en = en
        self.pwm_frequency = pwm_frequency

        self.motorIn1 = DigitalOutputDevice(self.in1)
        self.motorIn2 = DigitalOutputDevice(self.in2)
        self.motorEn = PWMOutputDevice(self.en, frequency=self.pwm_frequency)

    def stop(self):
        print(f"{self.name} STOP")
        self.motorIn1.off()
        self.motorIn2.off()

    def set_speed(self, speed):
        if speed > 0.0:
            print(f"{self.name} FORWARD... SPEED: {speed}")
            self.motorIn1.on()
            self.motorIn2.off()
        elif speed < 0.0:
            print(f"{self.name} BACKWARD... SPEED: {speed}")
            self.motorIn1.off()
            self.motorIn2.on()
        else:
            self.stop()
        self.motorEn.value = speed

    def destroy(self):
        self.motorIn1.close()
        self.motorIn2.close()
