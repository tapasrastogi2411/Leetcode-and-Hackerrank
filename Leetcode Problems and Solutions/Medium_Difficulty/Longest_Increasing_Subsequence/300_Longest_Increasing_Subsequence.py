'''
Link to problem: https://leetcode.com/problems/longest-increasing-subsequence/
Difficulty level: Medium

Leetcode problem number 300: Longest Increasing Subsequence: Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
'''

from typing import List

# Use dynamic programming for this question. There can be multiple such increasing subseqeunces, we just care about the length of one such longest increasing subsequence
def lengthLIS(nums: List[int]) -> int:

    # Initialise our dp array which would store the length of the longest increasing subseqeunce formed by the number at the ith index. These are initialised with a value of 1, since that is the minimum length of a subsequence that can be formed by a single number
    LIS = [1] * len(nums)

    # This is a O(N^2) time complexity algorithm, for we are looping twice through the nums array. We loop through first from the last index towards the first index. And the second loop go towards the right starting from the index of the first loop. We want to go from the last index, which len(nums - 1) to the first index which is 0
    for i in range(len(nums) - 1, -1, -1): # This could actually also be len(nums) here

        for j in range(i + 1, len(nums)):

            # The condition to check that the subsequence/number I am checking is indeed an increasing subsequence
            print(i, nums[i])
            if nums[i] < nums[j]: 

                # The length of the longest subsequence at an index can be that number itself, or the the length when you include the next number in your subsequence, and you only want the length of the longest subsequence possible at that index, so you take the max
                LIS[i] = max(LIS[i], 1 + LIS[j])
    
    return max(LIS)

#  Testing
input_nums = [10,9,2,5,3,7,101,18]
print(lengthLIS(input_nums))