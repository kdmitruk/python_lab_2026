import curses
import math


def main(stdscr):
    def show_player(pos, symbol, ox, oy, view_height, view_width):
        py, px = pos
        py -= oy
        px -= ox
        if px >= 0 and px < view_width and py >= 0 and py < view_height:
            stdscr.addch(py, px, symbol)

    def display(info, grid,ox,oy, player1, player2):
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
        show_player(player1, '1', ox, oy, view_height, view_width)
        show_player(player2, '2', ox, oy, view_height, view_width)
        stdscr.addstr(max_y-1, 0, info)
        return ox,oy
    curses.mousemask(curses.ALL_MOUSE_EVENTS)
    stdscr.keypad(True)
    grid, player1, player2 = read_file("map.txt")
    shooter = player1
    target = player2
    ox = 0
    oy = 0
    mx = 0
    my = 0
    angle = 0
    while True:
        info = f"{"First" if shooter == player1 else "Second"} player is up: {mx},{my},{angle}"
        ox,oy = display(info,grid,ox,oy, player1, player2)
        key = stdscr.getch()
        if key == curses.KEY_UP:
            oy -= 2
        elif key == curses.KEY_DOWN:
            oy += 2
        elif key == curses.KEY_LEFT:
            ox -= 4
        elif key == curses.KEY_RIGHT:
            ox += 4
        elif key == curses.KEY_MOUSE:
            _, mx, my, _, buttons = curses.getmouse()
            mx += ox
            my += oy
            if buttons & curses.BUTTON1_CLICKED:
                a = player1[0] - my
                b = mx - player1[1]
                angle = math.degrees(math.atan2(a,b))
        stdscr.refresh()

        shooter, target = target, shooter

def read_file(filename):
    grid = []
    with open(filename, "r") as file:
        for y, line in enumerate(file):
            line = line[:-1]

            for x, character in enumerate(line):
                if character == "1":
                    player1 = (y, x)
                if character == "2":
                    player2 = (y, x)
            row = [symbol == "X" for symbol in line]
            grid.append(row)

        return grid, player1, player2

if __name__ == '__main__':
    curses.wrapper(main)


