# Link to Problem: https://leetcode.com/problems/fibonacci-number/
# Difficulty - Easy

# Leetcode Problem number 509: Fibonacci Number: The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).


from typing import List, Tuple, Dict

# Attempting a dynammic programming approach through memoization
def fib_DP(n: int) -> int:
        
     # The format of a memo: key: nth fib number, value: the value of the nth fib number
    memo = {}
        
    # Checking if the number we are at is already computed and stored in the memo or not. And if it is, we just directly return it 
    if n in memo:
        return memo[n] # memo[n] stores the value of the nth fibonacci number
    
    # Otherwise we continue with normal recursive fibonacci
    if n < 2:
        result = n
        
    else: 
        result = fib_DP(n - 2) + fib_DP(n - 1)
        
    # Now we store the result that we have
    memo[n] = result
        
    return result

# Testing area

input_number =  3

print(fib_DP(input_number))