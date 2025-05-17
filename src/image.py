import pygame

class Image:
    def __init__(self, value):
        self.value = value
        self.surface = None
        self.is_loaded = False

    def load(self):
        self.surface = pygame.image.load(self.value)
        self.is_loaded = True