import pygame

class Drawer:
    def draw_frame(ctx, drawable):
        pygame.draw.rect(ctx.surface, drawable.color, pygame.Rect(
            drawable.x,
            drawable.y,
            drawable.width,
            drawable.height
        ), 1)

    def draw_rectangle(ctx, drawable):
        x, y = ctx.get_position(drawable.x, drawable.y)

        pygame.draw.rect(ctx.surface, drawable.color, pygame.Rect(
            x,
            y,
            drawable.width,
            drawable.height
        ))

    def clear(ctx, window):
        pygame.draw.rect(ctx.surface, (0, 0, 0), pygame.Rect(
            0,
            0,
            window.width,
            window.height
        ))

    def draw(ctx, drawable):
        drawable.draw(ctx, Drawer)

class Drawable:
    def __init__(self, x, y, color, width, height):
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height

    def draw(self, drawer: Drawer):
        pass