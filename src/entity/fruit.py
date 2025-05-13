from src.entity.object import Object
from src.entity.player import Player

class Fruit(Object):
    def __init__(self, x, y):
        super().__init__(x, y, (100, 0, 100), 40, 40)
    def on_collide(self, game, entity):
        if isinstance(entity, Player):
            print("colidiu com o player")