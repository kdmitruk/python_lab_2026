import curses

def load_map(path):
    grid = []
    with open(path, "r") as file:
        for line in file:
            row = [symbol == "X" for symbol in line]
            grid.append(row)
    return grid

def main(stdscr):
    def display(grid, info):
        max_y, max_x = stdscr.getmaxyx()
        stdscr.erase()
        for y in range(0, max_y-2):
            row = grid[y]
            row = row[:max_x]
            row = ["#" if flag else " " for flag in row]
            row = "".join(row)
            stdscr.addstr(y, 0, row)
        stdscr.addstr(max_y - 1, 0, info)
    player1 = 1
    player2 = 2
    grid = load_map(path="map.txt")

    shooter = player1
    target = player2
    while True:
        info = f"{"First" if shooter == player1 else "Second"} player is up:"
        display(grid, info)
        stdscr.getch()
        shooter, target = target, shooter

if __name__ == '__main__':
    curses.wrapper(main)