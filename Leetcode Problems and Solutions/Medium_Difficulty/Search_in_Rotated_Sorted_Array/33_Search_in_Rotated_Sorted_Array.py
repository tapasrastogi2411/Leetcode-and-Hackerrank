'''
Link to problem: https://leetcode.com/problems/search-in-rotated-sorted-array/
Difficulty level: Medium

Leetcode problem number 33: Search in Rotated Sorted Array: There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
'''

from typing import List, Tuple, Dict

'''Since we have to do this in logarithmic time and we have an almost sorted array, think of doing a binary search for this problem. We know that this array was originally sorted, so can we use this to our advantage?

Since we have rotated an already sorted array, we have two halves which are on their own already sorted
 '''
def search(nums: List[int], target: int) -> int:
    pass

# Testing
input_nums = [4,5,6,7,0,1,2]
input_target = 0

print(search(input_nums, input_target))