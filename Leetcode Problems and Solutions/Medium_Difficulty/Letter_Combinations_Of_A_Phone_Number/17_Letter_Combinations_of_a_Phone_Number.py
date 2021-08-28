'''
Link to problem: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
Difficulty level: Medium

Leetcode problem number 17: Letter combinations of a phone number: Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
'''

from typing import List, Tuple, Dict

def generateCombinations(currentString: str, digitToChar: Dict[str, str], digits: str, index: int, result: List[str]) -> None:
    
    # Our Base case: If the string we are is same length as the input digits, it means we have one possible combination and we can add it our final result list
    if len(currentString) == len(digits):
        result.append(currentString)

    else:

        # Get the current digit that we are at in the input string
        currentDigit = digits[index]

        # Get the letters that the current digit maps to
        mappingForDigit = digitToChar[currentDigit]

        # We add each character to the current string, and increment index by 1 to go to the next digit in the input string, since each digit only contributes one digit
        for char in mappingForDigit:
            generateCombinations(currentString + char, digitToChar, digits, index + 1, result)


def letterCombinations(digits: str) -> List[str]:
    
    digitToChar = {

        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
        
    }

    # A variable to store the final list of possible letter combinations
    result = []

    # If the input is not empty, then we pen up a recursive backtracking solution
    if len(digits) != 0:

        # This is the recursive helper function which does most of the work and modifies the result list in place returning nothing
        generateCombinations("", digitToChar, digits, 0, result)


    return result
  
    

# Testing 

input_digits = "23"

print(letterCombinations(input_digits))