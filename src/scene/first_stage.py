from src.scene.scene import Scene

from src.entity.player import Player

class FirstStageScene(Scene):
    def __init__(self):
        super().__init__([
            Player(20, 20)
        ])