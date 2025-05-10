import pygame
from pygame.locals import *

from src.drawer import Drawer
from src.ctx import GameContext

from src.window import Window
from src.frame import Frame

from src.scene.menu import MenuScene

class Game():
    def __init__(self):
        self.window = Window(800, 800)
        self.frame = Frame(10, 10)
        self.ctx = GameContext(self.window, self.frame)

        self.scenes = [MenuScene()]
        self.current_scene = 0

    def next_scene(self):
        if len(self.scenes) > self.current_scene + 1:
            return
        self.current_scene = self.current_scene + 1 

    def has_scene(self):
        return len(self.scenes) > self.current_scene

    def get_scene(self):
        return self.scenes[self.current_scene]

    def on_tick(self):
        Drawer.clear(self.ctx, self.window)
        Drawer.draw(self.ctx, self.frame)

        if self.has_scene():
            scene = self.get_scene()
            scene.init(self)
            

        for event in pygame.event.get():
            if event.type == QUIT:
                self.ctx.close()

    def start(self):
        self.ctx.start()

        while self.ctx.is_running:
            self.ctx.clock.tick(60)
            self.on_tick()
            pygame.display.update()
