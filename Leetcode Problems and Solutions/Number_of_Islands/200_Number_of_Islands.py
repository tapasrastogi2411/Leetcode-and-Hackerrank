# Link to Problem: https://leetcode.com/problems/number-of-islands/
# Difficulty - Medium

# Leetcode Problem number 200: Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

from typing import List, Tuple, Dict

def numIslands(grid: List[List[int]]) -> int:
    pass

# Testing

input_grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

print(numIslands(input_grid))