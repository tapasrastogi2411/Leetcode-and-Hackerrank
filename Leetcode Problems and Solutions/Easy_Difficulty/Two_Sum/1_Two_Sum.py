# Link to Problem: https://leetcode.com/problems/two-sum/
# Difficulty - Easy

# Leetcode Problem number 1: Two Sum - Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

from typing import List, Tuple, Dict

# This is a O(N^2) solution which works using a nested for loop 
def twoSumVersion1(nums: List[int], target: int) -> List[int]:
    for index1 in range(len(nums)):
        for index2 in range(index1 + 1, len(nums)):
            if nums[index1] + nums[index2] == target:
                return [index1, index2]


 
# Using a dictionary in this case to get the case which involves duplicates in the list and an O(N) solution as well
def twoSumVersion2(nums: List[int], target: int) -> List[int]:

    difference_dict = {}

    for index in range(len(nums)):

        if nums[index] not in difference_dict:
            
            difference = target - nums[index]
            difference_dict[difference] = index
        else:
            return [difference_dict[nums[index]], index]


# Trying out a O(N^2) solution to this problem
# This version works only if there are no duplicate items in the list    
def twoSumVersion3(nums: List[int], target: int) -> List[int]:

    # Initialising an empty list to store the indices
    index_list = []

    # Looping through the list to find the two numbers which sum to target
    for number1 in nums:
        for number2 in nums:
            if number1 != number2 and number1 + number2 == target:

                # Getting the index of the two numbers
                index1 = nums.index(number1)
                index2 = nums.index(number2)

                # Appending the indices of the two numbers found to the index_list initialised earlier
                index_list.append(index1)
                index_list.append(index2)

                # Returning the index_list as wanted after populating it
                return index_list
            
# Testing the code from this point
input_list = [2 ,2]
input_target = 4

print(twoSumVersion2(nums=input_list, target=input_target))
        
