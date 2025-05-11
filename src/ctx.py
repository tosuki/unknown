import pygame
from pygame.locals import *

class GameContext:
    def __init__(self, window, frame):
        self.surface = pygame.display.set_mode((window.width, window.height), HWSURFACE)
        self.frame = frame
        self.clock = pygame.time.Clock()
        self.font = None
        self.is_running = False

    def is_font_initialized(self):
        return not not self.font

    def load_font(self):
        self.font = pygame.font.SysFont(None, 24)

    def get_position(self, x, y):
        return self.frame.get_position(x, y)

    def close(self):
        self.is_running = False

    def start(self):
        self.is_running = True
        pygame.init()
        pygame.font.SysFont(None, 24)