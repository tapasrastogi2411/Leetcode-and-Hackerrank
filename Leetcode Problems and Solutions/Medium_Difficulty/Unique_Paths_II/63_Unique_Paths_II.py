'''
Link to problem: https://leetcode.com/problems/unique-paths-ii/
Difficulty level: Medium

Leetcode problem number 63: Unique paths: A robot is located at the top-left corner of a m x n grid

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and space is marked as 1 and 0 respectively in the grid.
'''
from typing import List

def uniquePathsWithObstacles(obstacleGrid: List[List[int]]) -> int:

    # Getting the number of rows and columns in our grid
    numRows = len(obstacleGrid)
    numColumns = len(obstacleGrid[0])
        
    # Initialising the dp_array as done in unique paths I problem
    dp_array = []
        
    for _ in range(numRows):
        dp_array.append([0] * numColumns)
        
    # Simplest case handled first
    if obstacleGrid[0][0] == 1:
            return 0
        
    dp_array[0][0] = 1
        
    # Calculating the number of ways to reach cell in the first row
    for i in range(1, numColumns):
            
        if obstacleGrid[0][i] == 1:
            dp_array[0][i] = 0
            
        else:
            dp_array[0][i] = dp_array[0][i - 1]
            
    # Calculating the number of ways to reach cells in the first column
    for i in range(1, numRows):
        if obstacleGrid[i][0] == 1:
                
            dp_array[i][0] = 0
           
        else:
            dp_array[i][0] = dp_array[i - 1][0]
        
        
    for i in range(1, numRows):
        for j in range(1, numColumns):

            if obstacleGrid[i][j] == 0:
            
                dp_array[i][j] = dp_array[i - 1][j] + dp_array[i][j - 1]
            
            else:
                dp_array[i][j] = 0
        
    return dp_array[numRows - 1][numColumns - 1]

# Testing

input_grid = [

    [0,0,0],
    [0,1,0],
    [0,0,0]

    ]

print(uniquePathsWithObstacles(input_grid))