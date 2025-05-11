import pygame

class Drawer:
    def draw_frame(ctx, drawable):
        pygame.draw.rect(ctx.surface, drawable.color, pygame.Rect(
            drawable.x,
            drawable.y,
            drawable.width,
            drawable.height
        ), 1)

    def draw_text(ctx, text: str, foreground, x, y):
        if not ctx.is_font_initialized():
            print("Initializing font!")
            ctx.load_font()
            return

        tx, ty = ctx.get_position(x, y)    
        text_surface = ctx.font.render(text, True, foreground)
        ctx.surface.blit(text_surface, (tx, ty))

    def draw_button(ctx, button):
        Drawer.draw_rectangle(ctx, button)
        Drawer.draw_text(ctx, button.text, button.text_color, button.x + 20, button.y + button.height /2)

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

    def on_tick(self, game):
        pass

    def draw(self, ctx, drawer: Drawer):
        pass