'''
Link to problem: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
Difficulty level: Medium

Leetcode problem number 34: First and last position of element in sorted array: There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
'''

from typing import List, Tuple, Dict

def searchRange(nums: List[int], target: int) -> List[int]:
    pass

# Testing
input_list = [5, 7, 7, 8, 8, 10]
input_target = 8

print(searchRange(input_list, input_target))