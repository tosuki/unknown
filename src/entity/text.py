from src.entity.entity import Entity

class Text(Entity):
    def __init__(self, text, x, y, color, text_color):
        super().__init__(x, y, color, 0, 0)
        self.text = text
        self.text_color = text_color

    def draw(self, ctx, drawer):
        return drawer.draw_text(ctx, self.text, self.text_color, self.x, self.y)