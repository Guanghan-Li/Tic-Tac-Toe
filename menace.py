import random

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
    return board.hash() in self.matchboxes

  def readBoard(self, board):
    if not self.isKnown(board):
      self.matchboxes[board.hash()] = board.possibleMoves()
    
    moves = self.matchboxes[board.hash()]
    return moves
  
  def getRotations(self, board):
    boardR1 = board.rotate()
    boardR2 = boardR1.rotate()
    boardR3 = boardR2.rotate()
    boardF = board.flip()
    boardFR1 = boardF.rotate()
    boardFR2 = boardFR1.rotate()
    boardFR3 = boardFR2.rotate()

    return [board, boardR1, boardR2, boardR3, boardF, boardFR1, boardFR2, boardFR3]
  
  def translateMove(known_board, unknown_board):
    pass


  def makeMove(self, board):
    moves = self.readBoard(board)
    move = random.choice(moves)
    self.made_moves[board.hash()] = move
    x, y = move
    board.addPiece(y, x, self.piece)