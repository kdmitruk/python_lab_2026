import curses

def main(stdscr):
    player1 = 1
    player2 = 2

    shooter = player1
    target = player2
    while True:
        info = f"{"First" if shooter == player1 else "Second"} player is up:"
        max_y, max_x = stdscr.getmaxyx()
        stdscr.erase()
        stdscr.addstr(max_y-1, 0, info)
        stdscr.getch()
        shooter, target = target, shooter

if __name__ == '__main__':
    curses.wrapper(main)