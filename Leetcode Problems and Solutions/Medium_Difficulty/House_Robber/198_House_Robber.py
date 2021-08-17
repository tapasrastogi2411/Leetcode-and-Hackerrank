# Link to Problem: https://leetcode.com/problems/house-robber/
# Difficulty - Medium

# Leetcode Problem number 198: House Robber: You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

from typing import List, Tuple, Dict

def rob(nums: List[int]) -> int:
    # Note how we are skipping indices here -> 1 -> 3 -> 5 -> 7 or 2 -> 4 -> 6
        
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        # Initialise your dp array - We can copy over a 1D or a 2D array using nums[:] also
        
        # dp[i] is going to hold how much ever we can rob upto ith house
        dp_array = [0] * len(nums) 
        
        # For when the length of the array is > 2
        dp_array[0] = nums[0]
        
        # For the second house, we will choose the second house only if its higher than the first house. Otherwise we stick to the first house only. Basically we will go to the second house if its higher than the first house
        dp_array[1] = max(nums[0], nums[1])
        
        # Filling the dp_array starting from the third house
    
        for i in range(2, len(nums)):
            dp_array[i] = max(nums[i] + dp_array[i - 2], dp_array[i - 1])
        
        return dp_array[len(nums) - 1] # There are only len(nums) - 1 items in dp_array
    
# Testing

input_list = [2,1,1,2]

print(rob(input_list))

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]



# Incrdibly useless first try :')
    # sum1 = 0
    # sum2 = 0
    # for i in range(0, len(nums), 2):
    #     sum1 += nums[i]
        
    # for j in range(1, len(nums), 2):
    #     sum2 += nums[j]
    
    # maximum_sum = max(sum1, sum2)
    # if maximum_sum == sum1 and maximum_sum == sum2:
    #     # Then picking only adjacent houses most likely didnt work
    #     pass