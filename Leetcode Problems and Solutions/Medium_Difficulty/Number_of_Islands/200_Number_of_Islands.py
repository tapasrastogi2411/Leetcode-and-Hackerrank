# Link to Problem: https://leetcode.com/problems/number-of-islands/
# Difficulty - Medium

# Leetcode Problem number 200: Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

from typing import List, Tuple, Dict

def callDFS(grid: List[List[int]],  row: int, col: int):

    # Base case: All reasons why the recursion could stop: If index is out of bounds, index is negative or the cell is not an island
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] != '1':
        return

    # We change the cell from '1' to '0' since we have already visited it and dont want to double count
    grid[row][col] = '0'
    
    # Now we have to carry out DFS on in possible direction, up, down, right and left
    callDFS(grid, row + 1, col) # Up
    callDFS(grid, row - 1, col) # Down
    callDFS(grid, row, col + 1) # Right
    callDFS(grid, row, col - 1) # Left

def numIslands(grid: List[List[int]]) -> int:
    
    # Getting the number of rows and columns in our grid
    numRows = len(grid)
    numColumns = len(grid[0])

    islandCount = 0
    
    # Loop through each cell in the grid
    for i in range(numRows):
        for j in range(numColumns):

            # Condition for performing DFS is that if we are at an island
            if grid[i][j] == '1':

                # Carry out DFS on the each graph cell
                callDFS(grid, i, j)

                # Increase island count by 1
                islandCount += 1
    
    return islandCount

    
    

# Testing

input_grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

print(numIslands(input_grid))