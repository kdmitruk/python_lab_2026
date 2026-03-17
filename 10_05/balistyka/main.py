import curses

from game import Game

def main(stdscr):
    stdscr.keypad(True)
    game = Game(stdscr)
    game.run()
if __name__ == '__main__':
    curses.wrapper(main)