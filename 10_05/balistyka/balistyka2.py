import curses


def main(stdscr):
    stdscr.keypad(True)
    player1 = (0, 0)
    player2 = (0, 1)
    shooter = player1
    target = player2
    while True:
        info = f"{"First" if shooter == player1 else "Second"} player is up:"
        stdscr.erase()
        stdscr.addstr(0, 0, info)
        key = stdscr.getch()
        stdscr.refresh()

        shooter, target = target, shooter

if __name__ == '__main__':
    curses.wrapper(main)

