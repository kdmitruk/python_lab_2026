from map import Map

class Game:
    def __init__(self, stdscr):
            self.stdscr = stdscr
            self.map = Map("map.txt")

    def run(self):
        while True:
            pass