from src.drawer import Drawable

class Entity(Drawable):
    def __init__(self, x, y, color, width, height):
        super().__init__(x, y, color, width, height)

    @staticmethod
    def get_entity_identifier():
        return 0

    def on_tick(self, game):
        pass

    def on_mouse_button_down(self, game, e):
        pass

    def draw(self, ctx, drawer):
        return drawer.draw_rectangle(ctx, self)
    
class ImageEntity(Entity):
    def __init__(self, sprites, x, y, color, width, height):
        super().__init__(x, y, color, width, height)
        self.sprites = sprites

    def draw(self, ctx, drawer):
        return drawer.draw_image(ctx, self)