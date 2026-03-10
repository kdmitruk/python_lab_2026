import curses

def load_map(path):
    grid = []
    with open(path, "r") as file:
        for line in file:
            row = [symbol == "X" for symbol in line]
            grid.append(row)
    return grid

def main(stdscr):
    def display(grid, info, offset_x, offset_y):
        max_y, max_x = stdscr.getmaxyx()
        view_width = max_x
        view_height = max_y - 2
        grid_width = len(grid[0])
        grid_height = len(grid)
        offset_x = min(max(0, offset_x), grid_width - view_width)
        offset_y = min(max(0, offset_y), grid_height - view_height)
        stdscr.erase()
        for y in range(offset_y, view_height + offset_y):
            row = grid[y]
            row = row[offset_x:max_x + offset_x]
            row = ["#" if flag else " " for flag in row]
            row = "".join(row)
            stdscr.addstr(y - offset_y, 0, row)
        stdscr.addstr(max_y - 1, 0, info)
        return offset_x, offset_y
    player1 = 1
    player2 = 2
    grid = load_map(path="map.txt")

    shooter = player1
    target = player2
    offset_x, offset_y = 0,0
    while True:
        info = f"{"First" if shooter == player1 else "Second"} player is up:"
        offset_x, offset_y = display(grid, info, offset_x, offset_y)
        key = stdscr.getch()
        if key == curses.KEY_UP:
            offset_y -= 2
        elif key == curses.KEY_DOWN:
            offset_y += 2
        elif key == curses.KEY_LEFT:
            offset_x -= 4
        elif key == curses.KEY_RIGHT:
            offset_x += 4
        shooter, target = target, shooter

if __name__ == '__main__':
    curses.wrapper(main)