'''
Link to problem: https://leetcode.com/problems/maximum-subarray/
Difficulty level: Easy

Leetcode problem number 53: Maximum Subarray: Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.
'''

from typing import List, Tuple, Dict

def maxSubArray(nums: List[int]) -> int:

    '''This question is an example of Kadane's algorithm, where we do it in a single pass
        
    The max_sum is set to the first element in the beginning and at each step we decide 
    if we want to add the next number to our sum or start a new subarray. max_sum is the
    maximum of these two choices at each step '''
        
    max_sum = nums[0]
        
    # The current sum starts at the first element of the array
    current_sum = max_sum
        
    # Iterating through the array starting from the second element
    for i in range(1, len(nums)):
            
        # We can add the next element and grow our subarray
        choice1 = current_sum + nums[i]
            
        # Or we can start a new subarray starting from the next element
        choice2 = nums[i]
            
        # Our choice of sum would be the max of the two above
        current_sum = max(choice1, choice2)
            
        # Updating the max and seeing if we have reached the max sum till now or not
        max_sum = max(max_sum, current_sum)
        
    # Return the max sum at the end
    return max_sum
            
# Testing

input_nums = [-2,1,-3,4,-1,2,1,-5,4]

print(maxSubArray(input_nums))
