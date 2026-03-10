import curses

def main(stdscr):
    def display(info, grid,ox,oy):
        max_y, max_x = stdscr.getmaxyx()
        stdscr.erase()
        view_width = max_x
        view_height = max_y-2
        grid_width = len(grid[0])
        grid_height = len(grid)
        ox = min(max(0,ox),grid_width - view_width)
        oy = min(max(0,oy),grid_height - view_height)
        for y in range(oy,view_height + oy):
            row = ["#" if pos else " " for pos in grid[y]]
            row = row[ox:max_x + ox]
            row = "".join(row)
            stdscr.addstr(y-oy,0,row)
        stdscr.addstr(max_y-1, 0, info)
        return ox,oy
    stdscr.keypad(True)
    player1 = (0, 0)
    player2 = (0, 1)
    shooter = player1
    target = player2
    grid = read_file("map.txt")
    ox = 0
    oy = 0
    while True:
        info = f"{"First" if shooter == player1 else "Second"} player is up:"
        ox,oy = display(info,grid,ox,oy)
        key = stdscr.getch()
        if key == curses.KEY_UP:
            oy -= 2
        elif key == curses.KEY_DOWN:
            oy += 2
        elif key == curses.KEY_LEFT:
            ox -= 4
        elif key == curses.KEY_RIGHT:
            ox += 4
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


