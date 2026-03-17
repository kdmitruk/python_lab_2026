class View:
    def __init__(self,stdscr):
        self.stdscr=stdscr

    def size (self) :
        y,x = self.stdscr.getmaxyx()
        return x,y-2
    def draw(self,map, camera, bullet, info):
        max_x, max_y = self.size()
        grid_width = map.width()
        grid_height = map.height()
        offset_x=camera.x()
        offset_y=camera.y()
        offset_x = min(max(0, offset_x), grid_width - max_x)
        offset_y = min(max(0, offset_y), grid_height - max_y)
        self.stdscr.erase()
        for y in range(offset_y, max_y + offset_y):
            row = map.grid[y]
            row = row[offset_x:max_x + offset_x]
            row = ["#" if flag else " " for flag in row]
            row = "".join(row)
            self.stdscr.addstr(y - offset_y, 0, row)

        self.display_player(map.player1, "1", (offset_x, offset_y), max_x, max_y)
        self.display_player(map.player2, "2", (offset_x, offset_y), max_x, max_y)

        if bullet is not None:
            sx = int(bullet.x) - offset_x
            sy = int(bullet.y) - offset_y
            if 0 <= sy < max_y and 0 <= sx < max_x - 1:
                self.stdscr.addch(sy, sx, '*')

        self.stdscr.addstr(max_y, 0, info)

    def display_player(self,player,symbol,offset,view_width,view_height):
        px,py=player
        ox,oy=offset
        x=px-ox
        y=py-oy
        if 0<=x and x<view_width and 0<=y and y<view_height:
            self.stdscr.addch(y,x,symbol)
