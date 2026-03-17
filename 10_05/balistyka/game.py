from map import Map
from view import View

class Game:
    def __init__(self, stdscr):
            self.stdscr = stdscr
            self.map = Map("map.txt")
            self.view = View(stdscr)

    def run(self):
        while True:
            self.view.draw(self.map)
            key = self.stdscr.getch()