from src.scene.scene import Scene

from src.entity.player import Player
from src.entity.fruit import Fruit

class FirstStageScene(Scene):
    def __init__(self):
        super().__init__([
            Player(20, 20)
        ], [Fruit(80, 80), Fruit(140, 140)])
