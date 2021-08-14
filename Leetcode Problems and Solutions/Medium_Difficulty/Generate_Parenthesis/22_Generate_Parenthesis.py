# Link to Problem: https://leetcode.com/problems/generate-parentheses/
# Difficulty - Medium

# Leetcode Problem number 22: Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

from typing import List, Tuple, Dict

# Define a recursive helper function which we will use in the main `generateParentheses` function

def backtracking(resultList: List[str], parenthesis: str, numOpen: int, numClose: int, n: int):

    # resultList is the list to which we add out valid orderings of parenthesis
    # parenthesis is the valid ordering of parenthesis that we end up at each time
    # numOpen is the number of open parenthesis that we have at a certain point
    # numClose is the number of close parenthesis that we have at a certain point
    # n is the pairs of parenthesis made available to us

    if(len(parenthesis) == 2 *n):
        # This means that we have a valid ordering and can append it to our result list
        resultList.append(parenthesis)
        return # This is our base case
    
    if numOpen < n:
        # This means that we can add opening parenthesis to our current string of parenthesis
        backtracking(resultList, parenthesis + "(", numOpen + 1, numClose, n)
    
    if numClose < numOpen:
        # This means we can add a closing parenthesis to out current string of parenthesis
        backtracking(resultList, parenthesis + ")", numOpen, numClose + 1, n)

    
    pass

# The main function which will give the list of valid ordering of the parenthesis
def generateParentheses(n: int) -> List[str]:

    # We are only allowed n open parenthesis and n closing parenthesis

    # We can only add closing parenthesis when num(close) < num(open)

    # We can add opening parenthesis at any point as long as num(open) < n

    # Stopping condition, when we know that the ordering is valid: num(open) == num(close) == n - When we stop adding parenthesis
    
    # A list to hold the final ordering of parenthesis
    result = []

    backtracking(result, "", 0, 0, n) # Since we start with 0 open , 0 closed parenthesis and build from there
    return result



# Testing
input_number = 100

print(generateParentheses(input_number))