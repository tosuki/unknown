from src.drawer import Drawable

class EntityAttributes:
    def __init__(self, health, speed):
        self.health = health
        self.speed = speed

class Entity(Drawable):
    def __init__(self, x, y, attributes):
        super().__init__(x, y, (155, 155, 155), 40, 40)
        self.attributes = attributes

    def on_tick(self, game):
        pass

    def draw(self, ctx, drawer):
        return drawer.draw_rectangle(ctx, self)