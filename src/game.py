import pygame
from pygame.locals import *

from src.ctx import GameContext
from src.window import Window
from src.frame import Frame

class Game():
    def __init__(self):
        self.window = Window(800, 800)
        self.frame = Frame(400, 400, 10, 10)
        self.ctx = GameContext(self.window)

    def on_tick(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.ctx.close()

    def start(self):
        self.ctx.start()

        while self.ctx.is_running:
            self.ctx.clock.tick(60)
            self.on_tick()
            pygame.display.update()
