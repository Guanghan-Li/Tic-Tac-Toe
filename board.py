import copy

class Board:
  def __init__(self, board=None):
    self.board = [
      [' ', ' ', ' '],
      [' ', ' ', ' '],
      [' ', ' ', ' ']
    ]
    if board != None:
      self.board = board

  def __str__(self):
    vline = u' \u2503 '
    junc = u'\u254b'
    rows = [vline.join(row) for row in self.board]
    hline = u'\u2501'*(len(rows[0]))
    foo = list(hline)
    foo[2] = junc
    foo[6] = junc
    hline = ''.join(foo)
    rows.insert(1, hline)
    rows.insert(3, hline)
    return '\n'.join(rows)

  def checkRow(self, board, piece):
    for row in board:
      if row.count(piece) == 3:
        return True
      
    return False

  def checkColumn(self, piece):
    columns = [[], [], []]

    for row in self.board:
      columns[0].append(row[0])
      columns[1].append(row[1])
      columns[2].append(row[2])

    return self.checkRow(columns, piece)

  def checkDiagonal(self, piece):
    diagonal1 = [self.board[0][0], self.board[1][1], self.board[2][2]]
    diagonal2 = [self.board[0][2], self.board[1][1], self.board[2][0]]
    diagonals = [diagonal1, diagonal2]

    return self.checkRow(diagonals, piece)

  def checkWin(self, piece):
    return self.checkRow(self.board, piece) or self.checkColumn(piece) or self.checkDiagonal(piece)

  def addPiece(self, row, column, piece):
    self.board[row][column] = piece
  
  def rotate(self):
    board = copy.deepcopy(self.board)
    board = list(zip(*board[::-1]))
    board = [list(row) for row in board]
    return Board(board)
  
  def rotateAmount(self, amount):
    board = self.board

    for i in range(amount):
      board = self.rotate(board)
    
    return board

  def flip(self):
    board = copy.deepcopy(self.board)
    board[0], board[2] = board[2], board[0]
    return Board(board)

  def hash(self):
    data = ''
    for row in self.board:
      data+=''.join(row)
    
    output = ''
    for char in data:
      if char == 'X':
        output += "1"
      elif char == 'O':
        output += '2'
      else:
        output += '0'

    return int(output,3)

  def isTie(self):
    for row in self.board:
      for col in row:
        if col == " ":
          return False
    return self.checkWin('X') == False and self.checkWin('O') == False

  def possibleMoves(self):
    moves = []
    for y in range(len(self.board)):
      for x in range(len(self.board)):
        if self.board[y][x] == ' ':
          moves.append((x,y))

    return moves
    
    return True and self.checkWin('X') == False and self.checkWin('O') == False
  
  def findAt(self):
    for y in range(3):
      for x in range(3):
        if self.board[y][x] == '@':
          return [x, y]

  def __eq__(self, other_board):
    return self.hash() == other_board.hash()
  
  