import pygame
from pygame.locals import *

from src.drawer import Drawer
from src.ctx import GameContext

from src.window import Window
from src.frame import Frame

from src.entity.player import Player

class Game():
    def __init__(self):
        self.window = Window(800, 800)
        self.frame = Frame(10, 10)
        self.ctx = GameContext(self.window, self.frame)

        self.entities = [Player(25, 25)]

    def on_tick(self):
        Drawer.clear(self.ctx, self.window)
        Drawer.draw(self.ctx, self.frame)

        for entity in self.entities:
            Drawer.draw(self.ctx, entity)
            entity.on_tick(self)

        for event in pygame.event.get():
            if event.type == QUIT:
                self.ctx.close()

    def start(self):
        self.ctx.start()

        while self.ctx.is_running:
            self.ctx.clock.tick(60)
            self.on_tick()
            pygame.display.update()
