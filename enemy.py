import random, math

class Enemy:
    def __init__(self):
        r = random.random() * 4
        if r > 3.0:
            self.x = 10
            self.y = int(random.random() * 800)
        elif r > 2.0:
            self.y = 10
            self.x = int(random.random() * 1200)
        elif r > 1.0:
            self.x = 1190
            self.y = int(random.random() * 800)
        else:
            self.y = 790
            self.x = int(random.random() * 1200)
        self.rot = 0
    def update(self):
        dx = 600 - self.x
        if dx == 0:
            dx = 1
        dy = 400 - self.y
        dx_ = dx / math.sqrt(dx * dx + dy * dy)
        dy_ = dy / math.sqrt(dx * dx + dy * dy)
        self.x = self.x + dx_
        self.y = self.y + dy_
        if dx > 0:
            self.rot = -90 - math.degrees(math.atan(dy / dx))
        else:
            self.rot = 90 - math.degrees(math.atan(dy / dx))
