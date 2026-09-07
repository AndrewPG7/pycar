from components.steer import Steer


class MockSteer(Steer):
    def __init__(self):
        self.direction = "Center" # Center: 0.0
        
    def reset(self):
        self.direction = "Center"
        print("Steering reset")
        
    def right(self):
        self.direction = "Right" # Right: +1.0
        print(f"Steering {self.direction}")
        
    def left(self):
        self.direction = "Left" # Left: -1.0
        print(f"Steering {self.direction}")