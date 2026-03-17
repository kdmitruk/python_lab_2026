class View:
    def __init__(self, stdscr):
        self.stdscr = stdscr
    def size(self):
        return self.stdscr.getmaxyx()
    def draw(self, map, camera, info):
        grid = map.grid
        offset_y = camera.y
        offset_x = camera.x
        max_y, max_x = self.size()
        view_width = max_x
        view_height = max_y - 2
        for y in range(offset_y, view_height + offset_y):
            row = grid[y]
            row = row[offset_x:max_x + offset_x]
            row = ["#" if flag else " " for flag in row]
            row = "".join(row)
            self.stdscr.addstr(y - offset_y, 0, row)
        self.stdscr.addstr(0, 0, f"{info}")
