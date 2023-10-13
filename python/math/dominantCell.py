#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'numCells' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY grid as parameter.
#

# fxn takes in a grid as parameter and return the number of dominant cells
def numCells(grid):
    # Write your code here

    #initialize variable to store the number of dominant cells
    dominant_cells = 0
    
    # get the number of rows and columns in the grid
    
    n = len(grid)
    m = len(grid[0])
    
    # loop over the number of rows and columns
    for i in range(n):
        for j in range(m):
            
            # get the value of the current cell
            val = grid[i][j]

            # check if the value is positive
            if val > 0:
                #assume the cell is positive untill proven otherwise
                dominant = True

                # get the list of valid neighbours of the cell
                neighbours_cells = get_neighbor(i, j, grid)
                
                # loop over the cells comparing neighbours values
                for x, y in neighbours_cells:
                    
                    #if any cell has greater or equal value, the cell is not dominant
                    if grid[x][y] >= val:
                        dominant = False
                        break
                    
              # if cell is dominant increase their total by 1
                if dominant:
                    dominant_cells +=1
    return dominant_cells

# helper function that return the valid neighbors of a cell in a grid
def get_neighbor(i, j, grid):
    
    # initialize an empty list
    neighbor = []

    #define the possible ofsets in row and column
    off_sets = [-1, 0, 1]
    
    # loop over the offsets and generate the neighbor cordinates
    for mx in off_sets:
        for ny in off_sets:
            
            #skip the cell itself
            if mx == 0 and ny ==0:
                continue
            
            # compute the new row and column indices
            x = i + mx
            y = j + ny
            
            # check if they are valid within the grid boundaries
            if 0 <=x < len(grid) and 0 <= y < len(grid[0]):

                #add the to the list of neigbour cells
                neighbor.append((x, y))
    return neighbor

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grid_rows = int(input().strip())
    grid_columns = int(input().strip())

    grid = []

    for _ in range(grid_rows):
        grid.append(list(map(int, input().rstrip().split())))

    result = numCells(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
