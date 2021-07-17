from board import Board
from menace import Menace
from player import Player
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
    playerX = Player('X')
    playerO = menaceO
    menace = menaceO
    db = dbO
  
  elif choice == 'O':
    playerO = Player('O')
    playerX = menaceX
    menace = menaceX
    db = dbX
  
  else:
    print("You have to enter 'X' or 'O'")


board = Board()
while board.checkWin("X") == False and board.checkWin('O') == False and board.isTie() == False:
  if board.checkWin("X") == False and board.checkWin('O') == False and board.isTie() == False:
    if type(playerX) is Player:
      print(board)
    playerX.makeMove(board)

  if board.checkWin("X") == False and board.checkWin('O') == False and board.isTie() == False:
    if type(playerO) is Player:
      print(board)
    playerO.makeMove(board)

  print('')

print(board)
if board.isTie():
  print("Tie!")
  playerO.learn("tie")
  playerX.learn('tie')
elif board.checkWin('X'):
  print("X won!")
  playerO.learn("lose")
  playerX.learn('win')
elif board.checkWin('O'):
  print("O won!")
  playerX.learn('lose')
  playerO.learn('win')

menace.saveState(db)

