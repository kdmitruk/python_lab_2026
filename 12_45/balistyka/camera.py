class Camera:
    def __init__(self):
        self.__x = 0
        self.__y = 0
        self.max_x = 1
        self.max_y = 1
    def set(self, x, y):
        self.__x = x
        self.__y = y
    def move(self, dx, dy):
        self.__x += dx
        self.__y += dy
    def set_max(self, x, y):
        self.max_x = x
        self.max_y = y
    def x(self):
        return self.__x - self.max_x//2
    def y(self):
        return self.__y - self.max_y//2
    def fix(self, grid_width, grid_height):
        grid_width  += self.max_x //2
        grid_height += self.max_y //2

        self.__x = min(max(self.max_x //2, self.__x), grid_width - self.max_x)
        self.__y = min(max(self.max_y //2, self.__y), grid_height - self.max_y)