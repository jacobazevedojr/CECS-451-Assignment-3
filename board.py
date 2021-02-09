import random
import numpy as np

# Utilizes encoding instead of grid
# Each index in "map" represents a row
# Each value in "map" represents column where a queen is present
class Board:
  def __init__(self, n):
    self.n_queen = n
    self.map = [-1 for i in range(n)]
    self.fit = 0

    for i in range(0, self.n_queen):
      j = random.randint(0, self.n_queen - 1)
      self.map[i] = j

# currently only accounts for same column or diagonal (is that enough?)
  def fitness(self):

    self.fit = 0     
    for i in range(self.n_queen):
      curr_queen = self.map[i]
      if curr_queen != -1:
        for j in range(1, self.n_queen - i):
          second_queen = self.map[i + j]
          # if the second queen is in the same column or diagonally right from og queen
          if second_queen == curr_queen or second_queen == curr_queen + j:
            self.fit += 1
          # else if the second queen is diagonally left from og queen
          elif (second_queen == curr_queen - j) and second_queen > -1:
            self.fit += 1
    return self.fit

  # show a grid view of the board
  def showGrid(self):
    grid = [[0 for i in range (self.n_queen)] for j in range (self.n_queen)]
    for i in range(self.n_queen):
      grid[i][self.map[i]] = 1
    for i in range(self.n_queen):
      print(grid[i])

  def show(self):
    print(self.map)

# TODO: Make sure flip function's used right
# (Also not sure if we need this, since Jacob has some flipping done in hillClimb)
  def flip(self, i, j):
    if self.map[i][j] == 0:
        self.map[i][j] = 1
    else:
        self.map[i][j] = 0

  def get_map(self):
    return self.map
  
  def get_fit(self):
    return self.fit

            
if __name__ == '__main__':
    test = Board(5)
    test.fitness()
    test.show()    
