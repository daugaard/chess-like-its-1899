from game.players import HumanPlayer
from game.game import Game

def run_console_game():
    white = HumanPlayer()
    black = HumanPlayer()

    game = Game(white, black)
    game.run()

if __name__ == "__main__":
    run_console_game()
