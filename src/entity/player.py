from src.entity.entity import Entity, EntityAttributes

class Attributes:
    def __init__(self, health, speed):
        self.health = health
        self.speed = speed

class Player(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, (155, 155, 155), 40, 40, EntityAttributes(
            health=20,
            speed=10
        ))
    def on_tick(self, game):
        print("hello world")