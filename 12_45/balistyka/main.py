import curses
from game import Game

def main(stdscr):
    curses.mousemask(curses.ALL_MOUSE_EVENTS)
    stdscr.timeout(15)

    game = Game(stdscr)
    game.run()

if __name__ == '__main__':
    curses.wrapper(main)