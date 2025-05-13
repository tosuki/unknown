from src.entity.entity import Entity
from src.collision import Collision

class Object(Entity):
    def __init__(self, x, y, color, width, height):
        super().__init__(x, y, color, width, height)

    def on_collide(self, game, entity):
        pass

    def check_collision(self, game, entity):
        if not Collision.check_collision(game.ctx, self, entity):
            return
        self.on_collide(game, entity)
        
    def on_tick(self, game):
        pass