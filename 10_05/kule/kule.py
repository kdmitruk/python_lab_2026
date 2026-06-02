import math

from direct.showbase.ShowBase import ShowBase
from panda3d.core import Vec3, Point2
from panda3d.core import AmbientLight, DirectionalLight, LVector3, LineSegs
from sympy import Point2D

from ball import Ball

class Game(ShowBase):
    PLANESIZE=5

    def __init__(self):
        super().__init__()
        self.disable_mouse()

        self.camera.set_pos(0, -15, 12)
        self.camera.look_at(0, 0, 0)

        ambient = AmbientLight('ambient')
        ambient.set_color((0.5, 0.5, 0.5, 1))
        self.render.set_light(self.render.attach_new_node(ambient))

        directional = DirectionalLight('directional')
        directional.set_color((1, 1, 1, 1))
        directional.set_direction(LVector3(-1, -1, -2))
        self.render.set_light(self.render.attach_new_node(directional))
        self.draw_bounds()
        self.add_balls()
        self.accept("mouse1", self.mouse_click)
        self.selectedBall = None
        self.accept("mouse1-up", self.mouse_up)
        self.taskMgr.add(self.update,"update")
        self.last_time = 0
        self.friction = 0.5
    def draw_bounds(self):
        lines=LineSegs()
        lines.moveTo(-Game.PLANESIZE,-Game.PLANESIZE,0)
        lines.drawTo(Game.PLANESIZE,-Game.PLANESIZE,0)
        lines.drawTo(Game.PLANESIZE,Game.PLANESIZE,0)
        lines.drawTo(-Game.PLANESIZE,Game.PLANESIZE,0)
        lines.drawTo(-Game.PLANESIZE,-Game.PLANESIZE,0)
        lines.set_color(1,1,1,1)
        model=lines.create()
        self.render.attach_new_node(model)

    def add_balls(self):
        self.balls = []
        ball = self.loader.loadModel("models/sphere.egg")

        begin = Vec3(-Game.PLANESIZE,-Game.PLANESIZE,0)
        end = Vec3(Game.PLANESIZE,Game.PLANESIZE,0)
        self.balls.append(Ball(begin, end, (1,0,0,1), ball, self.render))
        self.balls.append(Ball(begin, end, (0,0,1,1), ball, self.render))
        self.balls.append(Ball(begin, end, (0,1,0,1), ball, self.render))

    def update(self,task):
        dt = task.time - self.last_time
        self.last_time = task.time

        deceleration = self.friction * dt

        for ball in self.balls:
            distance = ball.velocity * dt
            ball.model.setPos(ball.model.getPos() + distance)

            speed = ball.velocity.length()
            if speed > 0:
                new_speed = speed - deceleration
                ball.velocity *= new_speed/speed


        return task.cont

    def mouse_up(self):
        try:
            pos = self.mouseWatcherNode.getMouse()
            px, py = pos.x, pos.y

        except:
            px, py = self.clickPos

        cx, cy = self.clickPos
        dx = px - cx
        dy = py - cy
        print(dx , dy)
        self.selectedBall.velocity = LVector3(dx,dy,0) * 5

    def mouse_click(self):
        pos = self.mouseWatcherNode.getMouse()
        self.clickPos = (pos.x, pos.y)
        print("x", pos)
        for ball in self.balls:
            ball_pos = ball.model.getPos(self.cam)
            point2 = Point2()
            self.camLens.project(ball_pos, point2)
            dist = math.hypot(point2.x - pos.x, point2.y - pos.y)
            if dist < 0.05:
                #print(ball.color)
                self.selectedBall = ball


if __name__ == '__main__':
    app = Game()
    app.run()