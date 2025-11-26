import chess
from game.players import PlayerInterface

class Game:
    def __init__(self, white: PlayerInterface, black: PlayerInterface):
        self.white = white
        self.black = black
        self.board = chess.Board()

    def run(self):
        print("Welcome!")
        while not self.board.is_game_over():
            print(self.board)  # optional: backend shouldn't print in future

            if self.board.turn == chess.WHITE:
                move = self.white.get_move(self.board)
            else:
                move = self.black.get_move(self.board)

            self.board.push(move)

        print("Game over:", self.board.result())
