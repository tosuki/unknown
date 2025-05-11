from src.scene.scene import Scene

from src.entity.text import Text

class IntroductionScene(Scene):
    def __init__(self):
        super().__init__([
            Text(
                text="Era uma vez sei lá o que, show de bola",
                x = 200,
                y = 200,
                color=(0, 0, 0),
                text_color=(255, 255, 255)
            )
        ])