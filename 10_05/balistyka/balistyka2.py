import curses

def main(stdscr):
    def display(info, grid):
        max_y, max_x = stdscr.getmaxyx()
        stdscr.erase()
        for y in range(max_y-2):
            row = ["#" if pos else " " for pos in grid[y]]
            row = row[:max_x]
            row = "".join(row)
            stdscr.addstr(y,0,row)
        stdscr.addstr(max_y-1, 0, info)
    stdscr.keypad(True)
    player1 = (0, 0)
    player2 = (0, 1)
    shooter = player1
    target = player2
    grid = read_file("map.txt")
    while True:
        info = f"{"First" if shooter == player1 else "Second"} player is up:"
        display(info,grid)
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
    curses.wrapper(main)


