from board import Board
from menace import Menace
from db import Database
import os

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
ties = 0
max_ties = 0
games = 0
while ties < 300:
  x_wins = 0
  o_wins = 0
  ties = 0
  for i in range(300):
    menaceO.made_moves = {}
    menaceX.made_moves = {}

    current_menace = menaceX
    other_menace = menaceO

    board = Board()

    while board.checkWin(other_menace.piece) == False and board.isTie() == False:
      current_menace.makeMove(board)
      other_menace, current_menace = current_menace, other_menace
    
    if board.isTie():
      ties += 1
      menaceX.learn("tie")
      menaceO.learn("tie")
    elif board.checkWin('X'):
      x_wins += 1
      menaceX.learn("win")
      menaceO.learn("lose")
    elif board.checkWin('O'):
      o_wins += 1
      menaceO.learn('win')
      menaceX.learn("lose")

  games += 300
    #print("Game:", i)

  if max_ties < ties:
    max_ties = ties
    print("Games Completed!")
    print("X Wins:", x_wins)
    print("O Wins:", o_wins)
    print("Ties", ties)
    print('Games Played:', games)

menaceO.saveState(dbO)
menaceX.saveState(dbX)