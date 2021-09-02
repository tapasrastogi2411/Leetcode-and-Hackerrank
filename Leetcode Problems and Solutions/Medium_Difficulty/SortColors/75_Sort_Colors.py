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

# Unbearably naive O(N) solution to this problem
def sortColorsNaive(nums: List[int]) -> None:

    # The different lists that we need for this question
    redList = []
    whiteList = []
    blueList = []

    # The list from which nums will copy the final answer
    newList = []
        
    # Building the individual 0s, 1s and 2s list
    for number in nums:
        if number == 0:
            redList.append(number)
            
        elif number == 1:
                
            whiteList.append(number)
            
        else:
            blueList.append(number)

    # Adding 0s, 1s, and 2s in the correct order to newList   
    for number in redList:
        newList.append(number)
        
    for number in whiteList:
        newList.append(number)
        
    for number in blueList:
        newList.append(number)
    
    # Copying the values from newList onto the input nums, since this is a in place question
    for index in range(len(newList)):
            
        nums[index] = newList[index]
        

# A better and simple O(N) solution to this problem.Also called the `Dutch Partitioning problem`

def sortColors(nums: List[int]) -> None:

    # Three variables, left, middle and right pointers for 0s, 1s and 2s respectively. Left and middle start at 0 and right pointer at the end
    left_pointer = 0
    middle_pointer = 0
    right_pointer = len(nums) - 1

    # The middle pointer is the one which is looped throughout the list

    while middle_pointer <= right_pointer:

        # If the element that you are at is a 0, then it should be at the beginning of the list, towards the left
        if nums[middle_pointer] == 0:

            # Since it is a 0, we swap this element with the element currently at the left position, using python notation
            nums[left_pointer], nums[middle_pointer] = nums[middle_pointer], nums[left_pointer]

            # We move both the left and the middle pointers forward
            left_pointer += 1
            middle_pointer += 1
        
        # If the element is a 1, then it should be in the middle, and we dont do anything
        elif nums[middle_pointer] == 1:

            # It is exactly where we want it to be, we just move on
            middle_pointer += 1
        
        # If the element is a 2, then it should be at the very end, towards the right
        else:

            # We swap it with the element at the right pointer
            nums[middle_pointer], nums[right_pointer] = nums[right_pointer], nums[middle_pointer]

            # We decrement the right pointer by 1
            right_pointer -= 1

            '''The reason we dont increment the middle pointer for this else clause, is because doing the swap above can introduce a 0 in the middle of the array, and moving the middle pointer by 1, leaves the possiblity of that being sranded somewhere in the middle with 1s and not at the beginning

            An example input demonstrating this: [0, 1, 2, 1, 0, 2]. This brings the value 0 in the middle of the array reaching the else clause, and if the middle pointer is incremented then we have the wrong input since the 0 is stuck in the middle of the array and not at the beginning

            '''



        
    
    

# Testing

input_nums = [0, 1, 2, 1, 0, 2]

print(input_nums)
sortColors(input_nums)
print(input_nums)
