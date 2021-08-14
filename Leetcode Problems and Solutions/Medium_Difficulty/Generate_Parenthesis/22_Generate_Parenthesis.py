# Link to Problem: https://leetcode.com/problems/generate-parentheses/
# Difficulty - Medium

# Leetcode Problem number 22: Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

from typing import List, Tuple, Dict

# Define a recursive helper function which we will use in the main `generateParentheses` function

def backtracking(numOpen: int, numClose: int):
    pass

# The main function which will give the list of valid ordering of the parenthesis
def generateParentheses(n: int) -> List[str]:

    # We can only add closing parenthesis when num(close) < num(open)

    # We can add opening parenthesis at any point as long as num(open) < n

    # Stopping condition, when we know that the ordering is valid: num(open) == num(close) == n - When we stop adding parenthesis

    # A stack to hold parenthesis
    stack = []
    
    # A list to hold the final ordering of parenthesis
    result = []



# Testing
input_number = 3

print(generateParentheses(input_number))