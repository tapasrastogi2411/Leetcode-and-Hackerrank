'''
Link to problem: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
Difficulty level: Medium

Leetcode problem number 17: Letter combinations of a phone number: Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
'''

from typing import List, Tuple, Dict

def generateCombinations(currentString: str, digitToChar: Dict[str, str], digits: str, index: int, result: List[str]) -> None:
    
    if len(currentString) == len(digits):
        result.append(currentString)

    else:

        currentDigit = digits[index]
        mappingForDigit = digitToChar[currentDigit]

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

    result = []

    if len(digits) != 0:

        generateCombinations("", digitToChar, digits, 0, result)


    return result
  
    

# Testing 

input_digits = "23"

print(letterCombinations(input_digits))