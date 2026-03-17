import math


class Bullet:
    GRAVITY    = 9.81

    def __init__(self, angle_rad, speed, x, y):
        self.x0  = float(x)
        self.y0  = float(y)
        self.vx0 = math.cos(angle_rad) * speed
        self.vy0 = math.sin(angle_rad) * speed
        self.t   = 0
        self.x   = self.x0
        self.y   = self.y0

    def step(self, game_map):
        self.t += 0.1
        self.x = self.x0 + self.vx0 * self.t
        self.y = self.y0 - self.vy0 * self.t + 0.5 * self.GRAVITY * self.t ** 2
        #return game_map.is_wall(self.y, self.x)