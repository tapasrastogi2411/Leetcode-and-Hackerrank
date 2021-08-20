'''
Link to problem: https://leetcode.com/problems/rotate-image/
Difficulty level: Medium

Leetcode problem number 48: Rotate image: You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation
'''

from typing import List, Tuple, Dict

# A 32 ms accepted solution with detailed explanation
def rotate(matrix: List[List[int]]) -> None:

    length = len(matrix)
        
    '''
    Rotating 90 degrees clockwise means that we have to transpose first and then 
    reflecting
    '''      
        
    for i in range(length):
        for j in range(i):
                
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
        
    '''Now we reflect the matrix from the right to the left. This is similar to iterative
    version of checking if a string was a palindrome where we loop till n // 2 and 
    check the first element with the last element, the second element with the second 
    last element and so on, till the middle element
        
    Reflecting here basically means switching the first element with the last element
    and so on
    '''
        
    for i in range(length):
        for j in range(length // 2):
                
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][length - j - 1] # similar to [n - i - 1]
            matrix[i][length - j - 1] = temp

# Testing

input_matrix = [

    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotate(input_matrix)

print(f"Rotate matrix is: {input_matrix}")