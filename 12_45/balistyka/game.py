from map import Map

class Game:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        map = Map("map.txt")
    def run(self):
        while True:
            key = self.stdscr.getch()