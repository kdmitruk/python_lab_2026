import curses
import math


def load_map(path):
    grid = []
    player1 = None
    player2 = None

    with open(path, "r") as file:
        for y,line in enumerate(file):
            for x,symbol in enumerate(line):
                if symbol == "1" :
                    player1 = (x,y)
                if symbol == "2":
                    player2=(x,y)

            row = [symbol == "X" for symbol in line]
            grid.append(row)
    return grid,player1,player2

def main(stdscr):
    def display_player(player,symbol,offset,view_width,view_height):
        px,py=player
        ox,oy=offset
        x=px-ox
        y=py-oy
        if 0<=x and x<view_width and 0<=y and y<view_height:
            stdscr.addch(y,x,symbol)


    def display(grid, info, offset_x, offset_y,player1,player2):
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
        display_player(player1,"1",(offset_x,offset_y),view_width,view_height)
        display_player(player2,"2",(offset_x,offset_y),view_width,view_height)
        stdscr.addstr(max_y - 1, 0, info)
        return offset_x, offset_y
    grid,player1,player2 = load_map(path="map.txt")
    curses.mousemask(curses.ALL_MOUSE_EVENTS)
    shooter = player1
    target = player2
    offset_x, offset_y = 0,0
    mx = 0
    my = 0
    angle = 0
    while True:
        info = f"{"First" if shooter == player1 else "Second"} player is up:"
        info += f" {mx} {my} {angle}"
        offset_x, offset_y = display(grid, info, offset_x, offset_y,player1,player2)
        key = stdscr.getch()
        if key == curses.KEY_UP:
            offset_y -= 2
        elif key == curses.KEY_DOWN:
            offset_y += 2
        elif key == curses.KEY_LEFT:
            offset_x -= 4
        elif key == curses.KEY_RIGHT:
            offset_x += 4
        elif key == curses.KEY_MOUSE:
            _,mx,my,_,buttons = curses.getmouse()
            mx += offset_x
            my += offset_y
            shooter, target = target, shooter
            dx = mx - shooter[0]
            dy = shooter[1] - my
            angle = math.degrees(math.atan2(dy,dx))
if __name__ == '__main__':
    curses.wrapper(main)