from components.light import Light


class MockLight(Light):
    def __init__(self, name):
        self.name = name
        self.is_on = False
        
    def on(self):
        self.is_on = True
        print(f"{self.name} turned on")
        
    def off(self):
        self.is_on = False
        print(f"{self.name} turned off")