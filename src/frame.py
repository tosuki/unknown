from src.window import Window

class Frame(Window):
    def __init__(self, width, height, x, y):
        super().__init__(width, height)
        self.x = x
        self.y = y

    def parse_coordinates(self, x, y):
        return (self.parse_x(x), self.parse_y(y))

    def parse_x(self, x):
        return self.x + x
    def parse_y(self, y):
        return self.y + y