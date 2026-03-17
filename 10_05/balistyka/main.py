import curses

from game import Game

def main(stdscr):
    game = Game(stdscr)
    key = stdscr.getch()
if __name__ == '__main__':
    curses.wrapper(main)