import curses
import math
import time

from PyQt5.QtGui import QMouseEvent

from map import Map
from view import View
from camera import Camera

class Game:
    def __init__(self, stdscr):
            self.stdscr = stdscr
            self.map = Map("map.txt")
            self.view = View(stdscr)
            self.camera = Camera(0, 0)
            self.press_time = None
            self.mouse_down = False
            self.info = ""

    def run(self):
        while True:
            #self.camera.set_max(*self.view.size())
            #self.camera.set(*self.map.player1)
            self.view.draw(self.map, self.camera, self.info)
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
                _, mx, my, _, buttons = curses.getmouse()
                mx += self.camera.x
                my += self.camera.y

                if buttons & curses.BUTTON1_PRESSED:
                    a = self.map.player1[0] - my
                    b = mx - self.map.player1[1]
                    self.angle = math.degrees(math.atan2(a, b))
                    self.mouse_down = True
                    self.press_time = time.time()

                elif buttons & curses.BUTTON1_RELEASED & self.mouse_down:
                    speed = time.time() - self.press_time
                    aim = (self.angle, speed, *self.map.player1)

                    self.info = f"{aim}"


