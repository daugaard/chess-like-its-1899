import abc
import chess


class PlayerInterface(abc.ABC):
    @abc.abstractmethod
    def get_move(self, board: chess.Board) -> chess.Move:
        pass


class HumanPlayer(PlayerInterface):
    def get_move(self, board: chess.Board) -> chess.Move:
        print("Your move in UCI e.g. (e2e4):")
        while(True): 
          move_str = input().strip()
          move = chess.Move.from_uci(move_str)
          if board.is_legal(move):
              return move
          else:
              print("Invalid move!")


