class Game:
    def __init__(self, stdscr):
        self.stdscr = stdscr
    def run(self):
        while True:
            key = self.stdscr.getch()