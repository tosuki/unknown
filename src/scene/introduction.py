from src.scene.scene import Scene

from src.entity.text import Text
from src.entity.button import Button

class IntroductionScene(Scene):
    def __init__(self):
        super().__init__([
            Text(
                text="Era uma vez sei lá o que, show de bola",
                x = 10,
                y = 200,
                color=(0, 0, 0),
                text_color=(255, 255, 255)
            ),
            Button(
                text="next",
                x = 10,
                y = 250,
                color=(255, 255, 255),
                text_color=(0,0,0),
                width=250,
                height=40,
                onclick=lambda game:
                    game.next_scene()
            )
        ])