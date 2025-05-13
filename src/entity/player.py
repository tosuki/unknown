import pygame
from src.entity.entity import Entity

class Attributes:
    def __init__(self, health, speed):
        self.health = health
        self.speed = speed

class Player(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, (155, 155, 155), 40, 40)
        self.attributes = Attributes(
            health=20,
            speed=5
        )

    def move_up(self, game):
        self.y = self.y - self.attributes.speed
    def move_down(self, game):
        self.y = self.y + self.attributes.speed
    def move_left(self, game):
        self.x = self.x - self.attributes.speed
    def move_right(self, game):
        self.x = self.x + self.attributes.speed

    def _handle_keys_pressed(self, game):
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_UP]:
            self.move_up(game)
        if keys_pressed[pygame.K_DOWN]:
            self.move_down(game)
        if keys_pressed[pygame.K_LEFT]:
            self.move_left(game)
        if keys_pressed[pygame.K_RIGHT]:
            self.move_right(game)
    
    def on_tick(self, game):
        self._handle_keys_pressed(game)

    def draw(self, ctx, drawer):
        return drawer.draw_rectangle(ctx, self)