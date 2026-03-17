class Map:
    def __init__(self, path):
        self.grid = []
        self.player1 = None
        self.player2 = None
        self.__load_map(path)
    def __load_map(self, path):
        with open(path, "r") as file:
            for y, line in enumerate(file):
                for x, symbol in enumerate(line):
                    if symbol == "1":
                        self.player1 = (x, y)
                    if symbol == "2":
                        self.player2 = (x, y)

                row = [symbol == "X" for symbol in line]
                self.grid.append(row)
    def height(self):
        return len(self.grid)
    def width(self):
        if len(self.grid) > 0:
            return len(self.grid[0])
        else:
            return 0