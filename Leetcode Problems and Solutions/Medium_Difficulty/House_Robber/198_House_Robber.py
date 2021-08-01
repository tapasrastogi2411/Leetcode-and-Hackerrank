# Link to Problem: https://leetcode.com/problems/house-robber/
# Difficulty - Medium

# Leetcode Problem number 198: House Robber: You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

from typing import List, Tuple, Dict

def rob(nums: List[int]) -> int:
    
    sum1 = 0
    sum2 = 0
    for i in range(0, len(nums), 2):
        sum1 += nums[i]
        
    for j in range(1, len(nums), 2):
        sum2 += nums[j]
    
    maximum_sum = max(sum1, sum2)
    if maximum_sum == sum1 and maximum_sum == sum2:
        # Then picking only adjacent houses most likely didnt work
        pass
    
# Testing

input_list = [2,1,1,2]

print(rob(input_list))