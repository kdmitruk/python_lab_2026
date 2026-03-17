import math
import time

from map import Map
from view import View
from camera import Camera
from bullet import Bullet

import curses
class Game:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.map = Map("map.txt")
        self.view = View(stdscr)
        self.camera = Camera()
        self.info = ""
        self.aim = None
        self.bullet = None
        self.speed = None

    def run(self):
        self.camera.set(*self.map.player1)
        while True:
            self.camera.set_max(*self.view.size())
            self.info = f"{self.camera.x()} {self.camera.y()} {self.aim}"
            self.view.draw(self.map, self.camera, self.bullet, self.info)
            key = self.stdscr.getch()
            if key == curses.KEY_UP:
                self.camera.move(0, -2)
            elif key == curses.KEY_DOWN:
                self.camera.move(0, 2)
            elif key == curses.KEY_LEFT:
                self.camera.move(-4, 0)
            elif key == curses.KEY_RIGHT:
                self.camera.move(4, 0)
            elif key == curses.KEY_MOUSE:
                self.handle_mouse()

            self.camera.fix(self.map.width(), self.map.height())

    def handle_mouse(self):
        _, mx, my, _, buttons = curses.getmouse()
        if buttons & curses.BUTTON1_PRESSED:
            mx += self.camera.x()
            my += self.camera.y()
            shooter = self.map.player1
            dx = mx - shooter[0]
            dy = shooter[1] - my
            angle = math.atan2(dy, dx)
            self.press_time = time.time()
            self.aim = (angle, None, shooter[0], shooter[1])

        elif buttons & curses.BUTTON1_RELEASED:
            speed =  time.time() - self.press_time
            self.aim = (self.aim[0], speed, self.aim[2], self.aim[3])
            self.bullet = Bullet(*self.aim)

    def __update_bullet(self):
        if self.bullet is None:
            return
        self.camera.set(self.bullet.x,self.bullet.y)
        self.bullet.step(self.map)
