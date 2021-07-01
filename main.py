from board import Board
from menace import Menace
from db import Database
import os

board = Board()
menaceO = Menace('O')
dbO = Database('databaseO.db')

if not os.path.exists(dbO.name):
  dbO.createDB()

menaceO.loadState(dbO)

current_piece = "X"

board = Board()
while board.checkWin("X") == False and board.checkWin('O') == False and board.isTie() == False:
  print(board)
  row = int(input("Choose a row 0-2: "))
  column = int(input("Choose a column 0-2: "))
  if board.board[row][column] == ' ':
    board.addPiece(row, column, 'X')
    if board.checkWin('X') == False and board.isTie() == False:
      menaceO.makeMove(board)
  else:
    print("Cant place there!")

  print('')

print(board)
if board.isTie():
  print("Tie!")
  menaceO.learn("tie")
elif board.checkWin('X'):
  print("X won!")
  menaceO.learn("lose")
elif board.checkWin('O'):
  print("O won!")
  menaceO.learn('win')

menaceO.saveState(dbO)