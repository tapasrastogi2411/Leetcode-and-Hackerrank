# Link to Problem: https://leetcode.com/problems/two-sum/
# Difficulty - Medium

# Leetcode Problem number 4: Median of Two Sorted Arrays - Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

from typing import List, Tuple, Dict
import math

def merge_two_sorted_lists(nums1: List[int], nums2: List[int]) -> List[int]:
    
    if(len(nums1) < len(nums2)):
        # We have to append nums1 elements to nums2
        for each_num in nums1:
            nums2.append(each_num)
        
        return nums2
    
    else:
        for each_num in nums2:
            nums1.append(each_num)
        
        return nums1
    
    

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:

    
    # Part 1 to consider: How to merge two uneven sorted lists
    # Try doing that through a helper function - merge_two_sorted_lists

    merged_list = merge_two_sorted_lists(nums1, nums2)
    sorted_merged_list = sorted(merged_list)
    
    if(len(sorted_merged_list)% 2 == 0):
        # We have an even numbered list, and median == (middle + (middle + 1) / 2) where middle == (len(list) // 2)  and (len(list) // 2) - 1
        index1 = len(sorted_merged_list) // 2
        index2 = index1 - 1
        
        number1 = sorted_merged_list[index1]
        number2 = sorted_merged_list[index2]

        median = (number1 + number2) / 2
        
    else:
        middleIndex = math.floor(len(sorted_merged_list) / 2)
        median = float(sorted_merged_list[middleIndex])
    
    return median

# Testing area

input_list1 = [1, 3]
input_list2 = [2]

# print(merge_two_sorted_lists(input_list1, input_list2))

print(findMedianSortedArrays(input_list1, input_list2))
