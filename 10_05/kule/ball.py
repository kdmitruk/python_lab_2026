import random

class Ball():
    def __init__(self, begin, end, color, model, parent):
        x = random.uniform(begin.x, end.x)
        y = random.uniform(begin.y, end.y)
        z = random.uniform(begin.z, end.z)
        self.model = model.copyTo(parent)
        self.model.setScale(0.1)
        self.model.setPos(x,y,z)
        self.model.setColor(*color)
        self.color = color

