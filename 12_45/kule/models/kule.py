from direct.showbase.ShowBase import ShowBase
from panda3d.core import AmbientLight, DirectionalLight, LVector3, LineSegs


class Game(ShowBase):
    LIMIT = 5

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

        self.add_bounds()

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



if __name__ == '__main__':
    app = Game()
    app.run()