from src.entity.entity import Entity, EntityAttributes

class Player(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, EntityAttributes(
            health=20,
            speed=10
        ))
    def on_tick(self, game):
        print("hello world")