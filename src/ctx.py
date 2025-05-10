import pygame
from pygame.locals import *

class GameContext:
    def __init__(self, window, frame):
        self.surface = pygame.display.set_mode((window.width, window.height), HWSURFACE)
        self.frame = frame
        self.clock = pygame.time.Clock()
        self.is_running = False

    def get_position(self, x, y):
        return self.frame.get_position(x, y)

    def close(self):
        self.is_running = False

    def start(self):
        self.is_running = True
        pygame.init()