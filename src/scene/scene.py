from src.drawer import Drawer

class Scene:
    def __init__(self, entities):
        self.entities = entities

    def init(self, game):
        for entity in self.entities:
            entity.on_tick(game)
            Drawer.draw(game.ctx, entity)