from src.drawer import Drawable

class Frame(Drawable):
    def __init__(self, x, y):
        super().__init__(x, y, (155, 200, 100), 400, 400)

    def draw(self, ctx, drawer):
        return drawer.draw_frame(ctx, self)