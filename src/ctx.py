import pygame
from pygame.locals import *

class GameContext:
    def __init__(self, window):
        self.surface = pygame.display.set_mode((window.width, window.height), HWSURFACE)
        self.clock = pygame.time.Clock()
        self.is_running = False

    def close(self):
        self.is_running = False

    def start(self):
        self.is_running = True
        pygame.init()