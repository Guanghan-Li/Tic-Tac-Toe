from board import Board
from menace import Menace
from db import Database
import os
x_wins = 0
o_wins = 0
ties = 0
board = Board()
menaceO = Menace('O')
dbO = Database('databaseO.db')

menaceX = Menace('X')
dbX= Database('databaseX.db')

if not os.path.exists(dbO.name):
  dbO.createDB()

menaceO.loadState(dbO)

if not os.path.exists(dbX.name):
  dbX.createDB()

menaceX.loadState(dbX)

current_menace = menaceX
other_menace = menaceO

for i in range(300):
  menaceO = Menace('O')
  menaceX = Menace('X')
  menaceO.loadState(dbO)
  menaceX.loadState(dbX)
  current_menace = menaceX
  other_menace = menaceO

  board = Board()
  while board.checkWin(other_menace.piece) == False and board.isTie() == False:
    #print(board)
    # row = int(input("Choose a row 0-2: "))
    # column = int(input("Choose a column 0-2: "))
    # if board.board[row][column] == ' ':
    #   board.addPiece(row, column, 'X')
    #   if board.checkWin('X') == False and board.isTie() == False:
    #     menace.makeMove(board)
    # else:
    #   print("Cant place there!")
    if board.checkWin(other_menace.piece) == False and board.isTie() == False:
      pass
      #current_menace.makeMove(board)
    current_menace.makeMove(board)
    #print('')
    other_menace, current_menace = current_menace, other_menace
  
  #print(board)
  if board.isTie():
    #print("Tie!")
    ties += 1
    menaceX.learn("tie")
    menaceO.learn("tie")
  elif board.checkWin('X'):
    #print("X won!")
    x_wins += 1
    menaceX.learn("win")
    menaceO.learn("lose")
  elif board.checkWin('O'):
    #print("O won!")
    o_wins += 1
    menaceO.learn('win')
    menaceX.learn("lose")

  print("Game:", i)
  menaceO.saveState(dbO)
  menaceX.saveState(dbX)

print("Games Completed!")
print("X Wins:", x_wins)
print("O Wins:", o_wins)
print("Ties", ties)