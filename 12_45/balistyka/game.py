from map import Map
from view import View
from camera import Camera
import curses
class Game:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.map = Map("map.txt")
        self.view = View(stdscr)
        self.camera = Camera()
        self.info = ""
    def run(self):
        self.camera.set(*self.map.player2)
        while True:
            self.camera.set_max(*self.view.size())
            self.info = f"{self.camera.x()} {self.camera.y()}"
            self.view.draw(self.map, self.camera, self.info)
            key = self.stdscr.getch()
            if key == curses.KEY_UP:
                self.camera.move(0, -2)
            elif key == curses.KEY_DOWN:
                self.camera.move(0, 2)
            elif key == curses.KEY_LEFT:
                self.camera.move(-4, 0)
            elif key == curses.KEY_RIGHT:
                self.camera.move(4, 0)
            self.camera.fix(self.map.width(), self.map.height())