import copy
from board import Board
from menace import Menace

data = [
  ['X', 'O', 'X'],
  [' ', 'X', 'O'],
  [' ', 'X', 'O']
]
board1 = Board(copy.deepcopy(data))
board2 = Board(copy.deepcopy(data))
board3 = board2.rotate()
board4 = board1.rotate()
board2.addPiece(1,0,'@')
print(board2.findAt())

print(board3.board)
print(board1)
print('')
print(board2)
print('')
print(board3)
print('')
print(board4)
print(board3.hash() == board4.hash())
