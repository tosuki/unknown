from src.scene.scene import Scene

from src.entity.player import Player

class MenuScene(Scene):
    def __init__(self):
        super().__init__([
            Player(10, 10)
        ])