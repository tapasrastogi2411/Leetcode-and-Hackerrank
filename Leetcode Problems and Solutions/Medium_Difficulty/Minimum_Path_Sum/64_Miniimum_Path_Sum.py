# Link to Problem: https://leetcode.com/problems/minimum-path-sum/
# Difficulty - Medium

# Leetcode Problem number 64: Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

from typing import List, Tuple, Dict

# This problem can be solved through Dynammic Programming
def minPathSum(grid: List[List[int]]) -> int:

    # Making a dynammic programming usable 2D list, which will be the size of our input grid. For any dynammic programming problem, our first step should be to initialise a `dp_array`

    # First we get the number of rows and columns which will be the dimension of your dp array

        # Getting the dimensions of the input grid
        numRows = len(grid)
        numColumns = len(grid[0])
        
        # Initialising the `dp array which we will use to get an O(N^2) solution
        dp_array = []
        # inner_rows = [0] * numColumns
        
        for i in range(numRows):
            dp_array.append([0] * numColumns)
        
            
        # Initialising the first cell of the dp_array which is the same as the first cell of the input grid
        dp_array[0][0] = grid[0][0]
        
        # Initialising the first row of the dp_array since there is only one way of reaching each cell in the first row = current cell value + previous cell value
        for i in range(1, numColumns):
            dp_array[0][i] = dp_array[0][i - 1] + grid[0][i] # Here grid[0][i] is the current cell we are at and dp_array[0][i - 1] is the previous cell
        
        
        # Initialising the first column of the dp_array since there is only one way to reach cell in the 
        for j in range(1, numRows):
            dp_array[j][0] = grid[j][0] + dp_array[j - 1][0]
        
        # Initialising all the other cells in the dp_array
        for i in range(1, numRows):
            for j in range(1, numColumns):
                dp_array[i][j] = grid[i][j] + min(dp_array[i - 1][j], dp_array[i][j - 1])
        
        # After filling up the dp_array, we are sure that the value at index [numRows - 1][numCols - 1],, that is the destination will have the minimum path value
        return dp_array[numRows - 1][numColumns - 1]
        
      


# Testing
# grid = [
#         [1,3,1],
#         [1,5,1],
#         [4,2,1]
#         ]

grid = [
                [3,8,6,0,5,9,9,6,3,4,0,5,7,3,9,3],
                [0,9,2,5,5,4,9,1,4,6,9,5,6,7,3,2],
                [8,2,2,3,3,3,1,6,9,1,1,6,6,2,1,9],
                [1,3,6,9,9,5,0,3,4,9,1,0,9,6,2,7],
                [8,6,2,2,1,3,0,0,7,2,7,5,4,8,4,8],
                [4,1,9,5,8,9,9,2,0,2,5,1,8,7,0,9],
                [6,2,1,7,8,1,8,5,5,7,0,2,5,7,2,1],
                [8,1,7,6,2,8,1,2,2,6,4,0,5,4,1,3],
                [9,2,1,7,6,1,4,3,8,6,5,5,3,9,7,3],
                [0,6,0,2,4,3,7,6,1,3,8,6,9,0,0,8],
                [4,3,7,2,4,3,6,4,0,3,9,5,3,6,9,3],
                [2,1,8,8,4,5,6,5,8,7,3,7,7,5,8,3],
                [0,7,6,6,1,2,0,3,5,0,8,0,8,7,4,3],
                [0,4,3,4,9,0,1,9,7,7,8,6,4,6,9,5],
                [6,5,1,9,9,2,2,7,4,2,7,2,2,3,7,2],
                [7,1,9,6,1,2,7,0,9,6,6,4,4,5,1,0],
                [3,4,9,2,8,3,1,2,6,9,7,0,2,4,2,0],
                [5,1,8,8,4,6,8,5,2,4,1,6,2,2,9,7]
        ]
print(minPathSum(grid))

# PROTIP: Code below to build a replica of a 2D array in python, where we want to copy the array `dp_array` from the 2D array `grid`

    # dp_array = []
    # for i in range(len(grid)):
    #     dp_array.append([])
    
    # for i in range(len(grid)):
    #     for j in range(len(grid[0])):
    #             dp_array[i].append(grid[i][j])

    
    # return dp_array
