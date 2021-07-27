# Link to Problem: https://leetcode.com/problems/valid-parentheses/
# Difficulty - Easy

# Leetcode Problem number 20: Valid Parenthesis - Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

from typing import List, Tuple, Dict

def isValid(s: str) -> bool:

    parenthesis_dict = {
        "[": "]",
        "{": "}",
        "(": ")"
    }

    # Implementing the stack as a python list
    stack = []

    # Loop through the input string
    for char in s:
        # Check to see if you have the opening bracket
        if char in parenthesis_dict:
            # If it is the opening bracket we push to the stack
            stack.append(char)
        
        # If the character is a closing bracket
        elif char in parenthesis_dict.values():

            # Two conditions to return false:

            # Either the stack is empty at this point, which means that we only have a closing bracket and not an opening bracket

            # If the closing bracket we are at doesnt match the opening bracket, since every closing bracket can only come after the same opening bracket for it to be valid. So the second condition is to check if the closing bracket and the previous opening bracket are of the same type.

            # parenthesis_dict[stack.pop()] gives the closing bracket that is expected for a valid combination, and we compare it with char which is the actual closing bracket we have in our input string

            # And we only have opening brackets in our stack, so we get it through pop operation. This step also removes the element from the stack
            if len(stack) == 0 or parenthesis_dict[stack.pop()] != char:
                return False

    return len(stack) == 0

# Testing
input_string1 = "()"
input_string2 = "()[]{}"
input_string3 = "(]"
input_string4 = "([)]"
input_string5 = "{[]}"


print(isValid(input_string1))
