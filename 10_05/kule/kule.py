from direct.showbase.ShowBase import ShowBase
from panda3d.core import Vec3
from panda3d.core import AmbientLight, DirectionalLight, LVector3, LineSegs
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
        #self.ball.reparentTo(self.render)
        #self.ball.setPos(2,0,0)
        #self.ball.setScale(0.1)
        #self.ball.setColor(1,0,0,1)
        begin = Vec3(-Game.PLANESIZE,-Game.PLANESIZE,0)
        end = Vec3(Game.PLANESIZE,Game.PLANESIZE,0)
        self.balls.append(Ball(begin, end, (1,0,0,1), ball, self.render))
        self.balls.append(Ball(begin, end, (0,0,1,1), ball, self.render))
        self.balls.append(Ball(begin, end, (0,1,0,1), ball, self.render))

if __name__ == '__main__':
    app = Game()
    app.run()