import math

from direct.showbase.ShowBase import ShowBase
from panda3d.core import AmbientLight, DirectionalLight, LVector3, LineSegs, Point2, Vec3, Vec2
from ball import Ball

class Game(ShowBase):
    LIMIT = 5
    FRICTION = 5

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

        self.selected_ball = None
        self.drag_start = None

        self.accept("mouse1", self.on_mouse_down)
        self.accept("mouse1-up", self.on_mouse_up)
        self.taskMgr.add(self.update, "update")

        self.add_bounds()
        self.add_balls()

        self.last_time = 0

    def add_bounds(self):
        lines = LineSegs()
        lines.moveTo(-Game.LIMIT,  Game.LIMIT, 0)
        lines.drawTo(-Game.LIMIT, -Game.LIMIT, 0)
        lines.drawTo( Game.LIMIT, -Game.LIMIT, 0)
        lines.drawTo( Game.LIMIT,  Game.LIMIT, 0)
        lines.drawTo(-Game.LIMIT,  Game.LIMIT, 0)

        lines.setThickness(5)
        node = lines.create()
        self.render.attach_new_node(node)

    def add_balls(self):
        ball = self.loader.loadModel("models/sphere")
        begin = LVector3(-Game.LIMIT, -Game.LIMIT, 0.2)
        end   = LVector3( Game.LIMIT,  Game.LIMIT, 0.2)

        self.balls = []

        self.balls.append(Ball.create_randomly_between(begin, end, ball, self.render, (1, 0, 0, 1)))
        self.balls.append(Ball.create_randomly_between(begin, end, ball, self.render, (0, 0, 1, 1)))
        self.balls.append(Ball.create_randomly_between(begin, end, ball, self.render, (1, 1, 0, 1)))

    def on_mouse_down(self):
        if not self.mouseWatcherNode.has_mouse(): return
        mouse_pos = self.mouseWatcherNode.get_mouse()
        self.drag_start = Vec2(mouse_pos.x, mouse_pos.y)
        print("Mouse", mouse_pos)
        for ball in self.balls:
            p3 = ball.model.getPos(self.camera)
            p2 = Point2()
            self.camLens.project(p3, p2)

            min_dist = 0.05
            dist = math.hypot(p2.x - mouse_pos.x, p2.y - mouse_pos.y)
            if dist < min_dist:
                print(ball.color)
                self.selected_ball = ball

    def on_mouse_up(self):
        if not self.mouseWatcherNode.has_mouse(): return
        if not self.selected_ball:
            return

        mouse_pos = self.mouseWatcherNode.get_mouse()

        print(self.drag_start, mouse_pos)

        dx = mouse_pos.x - self.drag_start.x
        dy = mouse_pos.y - self.drag_start.y

        self.selected_ball.velocity = Vec3(dx * 10, dy * 10, 0)
        print(self.selected_ball.velocity)
        self.selected_ball = None

    def update(self, task):
        time = task.time
        dt = time - self.last_time
        self.last_time = time

        friction = Game.FRICTION * dt

        for ball in self.balls:
            move = ball.velocity * dt
            pos = ball.model.getPos() + move
            ball.model.setPos(pos)

            if pos.x < -Game.LIMIT + Ball.RADIUS or pos.x > Game.LIMIT - Ball.RADIUS:
                ball.velocity.x *= -1
                pos.x = max(min(pos.x, Game.LIMIT - Ball.RADIUS), -Game.LIMIT + Ball.RADIUS)

            if pos.y < -Game.LIMIT + Ball.RADIUS or pos.y > Game.LIMIT - Ball.RADIUS:
                ball.velocity.y *= -1
                pos.y = max(min(pos.y, Game.LIMIT - Ball.RADIUS), -Game.LIMIT + Ball.RADIUS)

            speed = ball.velocity.length()

            if speed > 0:
                new_speed = speed - friction
                if new_speed > 0:
                    ball.velocity *= new_speed/speed
                else:
                    ball.velocity = LVector3(0, 0, 0)

        return task.cont




if __name__ == '__main__':
    app = Game()
    app.run()