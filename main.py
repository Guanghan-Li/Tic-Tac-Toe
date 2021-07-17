from board import Board
from menace import Menace
from db import Database
import os

board = Board()
menaceO = Menace('O')
dbO = Database('databaseO.db')
menaceX = Menace('X')
dbX = Database('databaseX.db')

if not os.path.exists(dbO.name):
  dbO.createDB()

if not os.path.exists(dbX.name):
  dbX.createDB()

menaceO.loadState(dbO)
menaceX.loadState(dbX)
choice = ''


while choice != 'X' and choice != 'O':
  choice = input('X or O? ')
  if choice == 'X':
    player_piece = "X"
    menace = menaceO
  
  elif choice == 'O':
    player_piece = 'O'
    menace = menaceX
  
  else:
    print("You have to enter 'X' or 'O'")

board = Board()
while board.checkWin("X") == False and board.checkWin('O') == False and board.isTie() == False:
  print(board)
  row = int(input("Choose a row 0-2: "))
  column = int(input("Choose a column 0-2: "))
  if board.board[row][column] == ' ':
    board.addPiece(row, column, player_piece)
    if board.checkWin(player_piece) == False and board.isTie() == False:
      menace.makeMove(board)
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

