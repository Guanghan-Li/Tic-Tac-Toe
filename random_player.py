import random

class RandomPlayer:
  def __init__(self, piece):
    self.piece = piece

  def makeMove(self, board):
    moves = board.possibleMoves()
    move = random.choice(moves)
    board.addPiece(move[1], move[0], self.piece)
