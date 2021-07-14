import random
from board import Board

class Menace:
  def __init__(self, piece):
    self.matchboxes = {}
    self.made_moves = {}
    self.piece = piece
  
  def loadState(self, db):
    self.matchboxes = db.load()
  
  def saveState(self, db):
    db.save(self.matchboxes)
  
  def addMoves(self, amount):
    for hash, move in self.made_moves.items():
      #if len(self.matchboxes[hash]) < 300:
      self.matchboxes[hash] += [move] * amount
  
  def removeMove(self):
    for hash, move in self.made_moves.items():
      if len(self.made_moves[hash]) > 2:
        self.matchboxes[hash].remove(move)

  def learn(self, result):
    if result == "win":
      self.addMoves(3)
    elif result == "tie":
      self.addMoves(1)
    elif result == "lose":
      self.removeMove()
    
  def isKnown(self, board):
    rotations = self.getRotations(board)

    for r in rotations:
      if r.hash() in self.matchboxes:
        return True
    
    return False

  def getKnownBoard(self, board):
    rotations = self.getRotations(board)

    for r in rotations:
      if r.hash() in self.matchboxes:
        return [board, r]
    
    return None

  def getMove(self, known_board):
    moves = self.matchboxes[known_board.hash()]
    move = random.choice(moves)
    return move  

  def readBoard(self, board):
    if not self.isKnown(board):
      self.matchboxes[board.hash()] = board.possibleMoves()
      move = self.getMove(board)
      return (move, move)
    else:
      known_board = self.getKnownBoard(board)[1]
      move = self.getMove(known_board)
      other_move = self.translateMove(known_board, board, move)
      return (move, other_move)
  
  def getRotations(self, board):
    boardR1 = board.rotate()
    boardR2 = boardR1.rotate()
    boardR3 = boardR2.rotate()
    boardF = board.flip()
    boardFR1 = boardF.rotate()
    boardFR2 = boardFR1.rotate()
    boardFR3 = boardFR2.rotate()

    return [board, boardR1, boardR2, boardR3, boardF, boardFR1, boardFR2, boardFR3]


  def translateMove(self, known_board: Board, unknown_board, move):
    x = move[0]
    y = move[1]
    known_board.addPiece(y, x, "@")
    rotations = self.getRotations(known_board)

    for r in rotations:
      if r == unknown_board:
        return r.findAt()


  def makeMove(self, board):
    data = self.readBoard(board)
    known_move = data[0]
    move = data[1]
    known_board = self.getKnownBoard(board)[1]
    self.made_moves[known_board.hash()] = known_move
    x, y = move
    board.addPiece(y, x, self.piece)