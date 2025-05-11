from src.drawer import Drawable

class Text(Drawable, ):
    def __init__(self, text, x, y, color, text_color):
        super().__init__(x, y, color, 0, 0)
        self.text = text
        self.text_color = text_color

    def draw(self, drawer):
        return drawer.draw_text(self.text, self.text_color, self.x, self.y)