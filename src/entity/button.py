from src.entity.entity import Entity

class Button(Entity):
    def __init__(self, text, onclick, x, y, color, text_color, width, height):
        super().__init__(x, y, color, width, height)
        self.text = text
        self.onclick = onclick
        self.text_color = text_color

    def _is_clicked(self, x, y):
        return (self.x <= x + self.width) and (self.y <= y <= self.y + self.height)

    def on_mouse_button_down(self, game, e):
        if e.button != 1:
            return
        x, y = e.pos

        if self._is_clicked(x, y) and self.onclick:
            self.onclick(game)

    def on_tick(self, game):
        pass

    def draw(self, ctx, drawer):
        drawer.draw_button(ctx, self)