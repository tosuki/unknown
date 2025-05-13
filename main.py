from src.game import Game
from src.window import Window
from src.frame import Frame

if __name__ == "__main__":
    game = Game(
        window=Window(1000, 800),
        frame=Frame(200, 100, 600, 600)
    )
    game.start()