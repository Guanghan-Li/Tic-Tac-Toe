import sqlite3

class Database:
  def __init__(self, name):
    self.name = name
  
  def createDB(self):
    db = sqlite3.connect(self.name)
    db.execute("create table menace (board integer, moves text)")
    db.close()
  
  def save(self, matchboxes):
    db = sqlite3.connect(self.name)
    cursor = db.cursor()

    for hash, moves in matchboxes.items():
      smoves = [str(move[0])+','+str(move[1]) for move in moves]
      smoves = '|'.join(smoves)
      cursor.execute("update menace set moves=(?) where board = (?)", (smoves, hash,))

      cursor.execute("insert into menace (board, moves) select ?, ? where (select Changes()=0)", (hash, smoves,))
     
    db.commit()
    db.close()

  def formatMove(self, move):
    move = move.split(',')
    move[0] = int(move[0])
    move[1] = int(move[1])
    return tuple(move)

  def load(self):
    matchboxes = {}
    db = sqlite3.connect(self.name)
    cursor = db.cursor()
    
    cursor.execute("select * from menace")
    data = cursor.fetchall()

    for row in data:
      if row[1] != '':
        moves = row[1].split('|')
        moves = [self.formatMove(move) for move in moves]
        matchboxes[row[0]] = moves

    return matchboxes
    