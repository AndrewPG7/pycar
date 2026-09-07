from components.motor import Motor


class MockMotor(Motor):
    def __init__(self, name):
        self.name = name
        self.speed = 0 # Stop: 0, Max forward: +1.0, Max reverse: -1.0
        
    def set_speed(self, speed):
        self.speed = speed
        print(f"{self.name} speed set to {self.speed}")
        
    def stop(self):
        self.set_speed(0.0)
        print(f"{self.name} stopped")