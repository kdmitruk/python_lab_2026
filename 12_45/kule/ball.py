import random
from panda3d.core import LVector3, Vec3


class Ball:
    def __init__(self, model, parent, pos, color):
        self.model = model.copyTo(parent)
        self.model.setScale(0.1)
        self.model.setPos(*pos)
        self.model.setColor(*color)
        self.color = color

        self.velocity = Vec3(0, 0, 0)

    @staticmethod
    def create_randomly_between(begin, end, model, parent, color):
        x = random.uniform(begin.x, end.x)
        y = random.uniform(begin.y, end.y)
        z = random.uniform(begin.z, end.z)
        return Ball(model, parent, (x, y, z), color)



