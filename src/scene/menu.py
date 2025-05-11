from src.scene.scene import Scene

from src.entity.button import Button

class MenuScene(Scene):
    def __init__(self):
        super().__init__([
            Button(
                text="start",
                x = 100,
                y = 200,
                width = 200,
                color = (255, 255, 255),
                text_color = (0, 0, 0),
                height = 40,
                onclick = lambda game:
                    game.next_scene()
            ),
            Button(
                text="exit",
                x = 100,
                y = 260,
                width = 200,
                color = (255, 255, 255),
                text_color = (0, 0, 0),
                height = 40,
                onclick = lambda game:
                    game.ctx.close()
            )
        ])