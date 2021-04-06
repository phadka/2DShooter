import math

class Bullet:
    def __init__(self, rot):
        self.rot = rot
        self.x = 600
        self.y = 400
        self.x = self.x - math.sin(math.radians(self.rot)) * 40
        self.y = self.y - math.cos(math.radians(self.rot)) * 40
    def update(self):
        self.x = self.x - math.sin(math.radians(self.rot)) * 25
        self.y = self.y - math.cos(math.radians(self.rot)) * 25
