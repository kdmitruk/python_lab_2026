import random

from panda3d.core import LVector3
from sympy.physics.units import velocity


class Ball():
    def __init__(self, begin, end, color, model, parent):
        x = random.uniform(begin.x, end.x)
        y = random.uniform(begin.y, end.y)
        z = random.uniform(begin.z, end.z)
        self.velocity = LVector3(0,0,0)
        self.model = model.copyTo(parent)
        self.model.setScale(0.1)
        self.model.setPos(x,y,z)
        self.model.setColor(*color)
        self.color = color


