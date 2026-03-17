import curses

from map import Map
from view import View
from camera import Camera

class Game:
    def __init__(self, stdscr):
            self.stdscr = stdscr
            self.map = Map("map.txt")
            self.view = View(stdscr)
            self.camera = Camera(0, 0)

    def run(self):
        while True:
            #self.camera.set_max(*self.view.size())
            #self.camera.set(*self.map.player1)
            self.view.draw(self.map, self.camera)
            key = self.stdscr.getch()
            if key == curses.KEY_UP:
                self.camera.move(0, -2)
            elif key == curses.KEY_DOWN:
                self.camera.move(0,  2)
            elif key == curses.KEY_LEFT:
                self.camera.move(-4, 0)
            elif key == curses.KEY_RIGHT:
                self.camera.move(4, 0)
            elif key == curses.KEY_MOUSE:
                pass