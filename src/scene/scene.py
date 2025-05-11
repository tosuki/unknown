import pygame
from pygame.locals import *

from src.drawer import Drawer

class Scene:
    def __init__(self, entities):
        self.entities = entities

    def init(self, game):
        for entity in self.entities:
            entity.on_tick(game)
            Drawer.draw(game.ctx, entity)

        for event in pygame.event.get():
            if event.type == QUIT:
                self.ctx.close()
            if event.type == MOUSEBUTTONDOWN:
                for entity in self.entities:
                    entity.on_mouse_button_down(game, event)