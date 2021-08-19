'''
Link to problem: https://leetcode.com/problems/unique-paths/
Difficulty level: Medium

Leetcode problem number 62: Unique paths: A robot is located at the top-left corner of a m x n grid

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
'''

def uniquePaths(m: int, n: int) -> int:
    numRows = m
    numColumns = n
        
    '''Initialise dp_array. dp_array[i][j] stores the number of ways to reach the [i][j]
    cell from the top-left starting point
    '''
    dp_array = []
        
    for _ in range(numRows):
        dp_array.append([0] * numColumns)
        
    # Filling the dp_array with values
    dp_array[0][0] = 1
        
    # There is only way to reach each cell in the first row from the top-left corner
    for i in range(1, numColumns):
        dp_array[0][i] = 1
        
    # There is only one way to reach each cell in the first column from the top-left corner
    for j in range(1, numRows):
        dp_array[j][0] = 1
        
    ''' For everry other cell in the grid, we can either reach it from the cell above it,
        denoted by [i - 1][j] or the from the cell to its right, denoted by [i][j - 1]
        
        This is because we are allowed only going down or to the right, so you can only reach
        a cell from the top or from the left
        
        This means that the number of ways to reach an inner cell [i][j] is the sum of the
        number of ways to reach it from the top and the number of ways to reach it from the
        left
    '''
        
    for i in range(1, numRows):
        for j in range(1, numColumns):
                
            dp_array[i][j] = dp_array[i-1][j] + dp_array[i][j - 1]
        
    # The answer will be the last cell, as we want the number of ways to reach the last cell
    return dp_array[numRows - 1][numColumns - 1] # can also be indexed as [-1][-1]
    

# Testing

print(uniquePaths(3, 7))