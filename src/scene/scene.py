from src.entity.player import Player
from src.drawer import Drawer

class Scene:
    def __init__(self, entities):
        self.entities = entities

    def init(self, game):
        for entity in self.entities:
            entity.on_tick(self, game)
            Drawer.draw(game.ctx, entity)