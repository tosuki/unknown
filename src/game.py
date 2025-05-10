import pygame
from pygame.locals import *

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class GameContext:
    def __init__(self, window: Window):
        self.surface = pygame.display.set_mode((window.width, window.height), HWSURFACE)
        self.clock = pygame.time.Clock()
        self.is_running = False

    def close(self):
        self.is_running = False

    def start(self):
        self.is_running = True
        pygame.init()

class Game():
    def __init__(self):
        self.window = Window(800, 800)
        self.frame = Window(400, 400)
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
