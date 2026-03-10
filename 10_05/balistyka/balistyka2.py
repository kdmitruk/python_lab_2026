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

def read_file(filename):
    grid = []
    with open(filename, "r") as file:
        for line in file:
            line = line[:-1]
            row = [symbol == "X" for symbol in line]
            grid.append(row)

        return grid

if __name__ == '__main__':
    read_file("map.txt")
    # curses.wrapper(main)

