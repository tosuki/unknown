import pygame
from pygame.locals import *

from src.drawer import Drawer

class Scene:
    def __init__(self, entities, objects = []):
        self.entities = entities
        self.objects = objects

    def check_collision(self, game):
        pass

    def init(self, game):
        for entity in self.entities:
            entity.on_tick(game)

            for object in self.objects:
                object.check_collision(game, entity)
                Drawer.draw(game.ctx, object)

            Drawer.draw(game.ctx, entity)


        for event in pygame.event.get():
            if event.type == QUIT:
                self.ctx.close()
            if event.type == MOUSEBUTTONDOWN:
                for entity in self.entities:
                    entity.on_mouse_button_down(game, event)