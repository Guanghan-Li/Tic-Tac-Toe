class Player:
  def __init__(self, piece):
    self.piece = piece
  
  def makeMove(self, board):
    row, column = -1, -1
    cell = '@'

    while cell != ' ':
      row = int(input("Choose a row 0-2: "))
      column = int(input("Choose a column 0-2: "))
      cell = board.board[row][column]
      if cell == ' ':
        board.addPiece(row, column, self.piece)
      else:
        print("Cant place there!")

  def learn(self, result):
    pass