# Link to Problem: https://leetcode.com/problems/two-sum/
# Difficulty - Medium

# Leetcode Problem number 704: Binary Search - Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

 # You must write an algorithm with O(log n) runtime complexity.


from typing import List, Tuple, Dict

def search(nums: List[int], target: int) -> int:
    
    left = 0
    right = len(nums) - 1

    while left <= right:

	    #Calculate middle number (mid)
        mid = (left+right) // 2
        print(f"nums[mid] = {mid}")
		#If mid is equal to target
        if nums[mid] == target:
             return mid

	    #If mid is greater than target then right is equal to the index before mid
        if nums[mid] > target:
             right = mid - 1

	    #If mid is less than target then left is equal to the index after mid
        else:
             left = mid + 1

	#If target is not found 
    return -1

# Testing area

input_list =  [-1,0,3,5,9,12]
input_target = 9

print(search(input_list, input_target))