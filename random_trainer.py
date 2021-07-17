from board import Board
from menace import Menace
from random_player import RandomPlayer
from db import Database
import os

board = Board()
menaceO = Menace('O')
dbO = Database('databaseO.db')

if not os.path.exists(dbO.name):
  dbO.createDB()

menaceO.loadState(dbO)

current_menace = RandomPlayer('X')
other_menace = menaceO
ties = 0
x_wins = 0
o_wins = 0
for i in range(30000):
  menaceX = RandomPlayer('X')
  menaceO.made_moves = {}
  current_menace = menaceX
  other_menace = menaceO

  board = Board()
  while board.checkWin(other_menace.piece) == False and board.isTie() == False:
    current_menace.makeMove(board)
    other_menace, current_menace = current_menace, other_menace
  
  if board.isTie():
    ties += 1
    menaceO.learn("tie")
  elif board.checkWin('X'):
    x_wins += 1
    menaceO.learn("lose")
  elif board.checkWin('O'):
    o_wins += 1
    menaceO.learn('win')

  #print("Game:", i)


print("Games Completed!")
print("X Wins:", x_wins)
print("O Wins:", o_wins)
print("Ties", ties)

menaceO.saveState(dbO)