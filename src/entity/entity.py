from src.drawer import Drawable

class Entity(Drawable):
    def __init__(self, x, y, color, width, height):
        super().__init__(x, y, color, width, height)

    def on_tick(self, game):
        pass

    def on_mouse_button_down(self, game, e):
        pass

    def draw(self, ctx, drawer):
        return drawer.draw_rectangle(ctx, self)