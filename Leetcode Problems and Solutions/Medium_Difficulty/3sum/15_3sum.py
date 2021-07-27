# Link to Problem: https://leetcode.com/problems/two-sum/
# Difficulty - Medium

# Leetcode Problem number 1: 3Sum - Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

from typing import List, Tuple, Dict


# PROTIP We dont really need line 63 - 70 in this since we only need to update either the left or the right pointer to change the value of three_sum. The other pointer is automatically updated by the if else block at line 39 - 47

def threeSum(nums: List[int]) -> List[List[int]]:

    # Have a result array
    result = []

    # Step 1: We need to sort the list to avoid having duplicates in our list
    nums = sorted(nums)

    # If nums[i] == nums[i - 1] then it means that this is a recipe for duplicates. And we know this since our array is sorted. We are eliminating duplicates by not re-using the same element again
    
    # We only have the choice of the first number from 0 to the second last
    for i in range(len(nums)):

        # The i > 0 condition is there to make sure that the loop iterates when i = 0 and doesnt skip this case because of nums[0 - 1] = nums[-1]. nums[-1] != nums[1] which we actually want

        # We only want to start checking for duplicates after the first element, that from i > 0 = 1
        if i > 0 and nums[i] == nums[i - 1]:

            continue # We dont need this case

        left_pointer = i + 1
        right_pointer = len(nums) - 1

        while(left_pointer < right_pointer):

            # We calculate the possible value of the threeSum we are at using values at i, left_pointer and right_pointer
            three_sum = nums[i] + nums[left_pointer] + nums[right_pointer]
            
            if three_sum > 0:

                # Need to reduce the sum, and since this is a sorted array, we can just reduce the right pointer by 1
                right_pointer -= 1

            elif three_sum < 0:

                # Need to increase the sum, and since this is a sorted array, we can just increase the left pointer by 1
                left_pointer += 1
            
            else:
                 
                # This means that sum == 0 and we have our correct triplet. We add the result to the output list
                result.append([nums[i], nums[left_pointer], nums[right_pointer]])
                
                # Now we move left pointer ahead to keep searching for our next iteration
                left_pointer += 1

                # We check if moving this left pointer ahead by one leaves us with the same number as before(The checking for duplicates point)
                while nums[left_pointer] == nums[left_pointer - 1] and left_pointer < right_pointer :

                    # if so, we skip that value and move on to the next one
                    left_pointer += 1

                # Similarly we move the right pointer to the left to keep searching for our next iteration 
                right_pointer -= 1

                # We check if moving this right pointer behind by one leaves us with the same number as before(The checking for duplicates point)
                while nums[right_pointer] == nums[right_pointer + 1] and left_pointer < right_pointer:

                    # if so, we skip that value and move on to the next one, this time backwards as right_pointer starts at the right end of the list
                    right_pointer -= 1
                
        
                
                
    return result



# Testing
input_list = [-2,0,3,-1,4,0,3,4,1,1,1,-3,-5,4,0]

print(threeSum(input_list))