class Camera:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_max(self, max_x, max_y):
        self.max_x = max_x
        self.max_y = max_y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def set(self, x, y):
        self.x = x #- self.max_x // 2
        self.y = y #- self.max_y // 2
