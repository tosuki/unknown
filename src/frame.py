from src.drawer import Drawable

class Frame(Drawable):
    def __init__(self, x, y):
        super().__init__(x, y, (155, 200, 100), 400, 400)

    def get_x(self, x):
        return self.x + x
    
    def get_y(self, y):
        return self.y + y

    def get_position(self, x, y):
        return (
            self.get_x(x),
            self.get_y(y)
        )
    
    def _check_real_position(self, drawable, callback):
        x, y = self.get_position(drawable.x, drawable.y)

        return callback(x, y)

    def is_at_horizontal_boundaries(self, drawable):
        return self._check_real_position(
            drawable,
            lambda x, _: x + drawable.width >= self.x + self.width or x <= self.x
        )

    def is_at_horizontal_boundaries(self, drawable):
        return self._check_real_position(
            drawable,
            lambda _, y: y + drawable.height >= self.y + self.width or y <= self.x
        )

    def draw(self, ctx, drawer):
        return drawer.draw_frame(ctx, self)