class View:
    def __init__(self, stdscr):
        self.stdscr = stdscr
    def size(self):
        return self.stdscr.getmaxyx()
    def draw(self, map):
        grid = map.grid
        offset_y = 0
        offset_x = 0
        max_y, max_x = self.size()
        view_width = max_x
        view_height = max_y - 2
        for y in range(offset_y, view_height + offset_y):
            row = grid[y]
            row = row[offset_x:max_x + offset_x]
            row = ["#" if flag else " " for flag in row]
            row = "".join(row)
            self.stdscr.addstr(y - offset_y, 0, row)