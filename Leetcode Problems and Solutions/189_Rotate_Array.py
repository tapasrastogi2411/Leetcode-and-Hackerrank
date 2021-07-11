# Link to Problem: https://leetcode.com/problems/rotate-array/
# Difficulty - Medium

# Leetcode Problem number 189: Rotate Array - Given an array, rotate the array to the right by k steps, where k is non-negative.

def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # Index for looping through as many times as the number of rotations
    index = 0
        
    # Loop set up
    for index in range(k):
            
        # Removing the element at the end of the list
        number_to_remove = nums.pop(len(nums) - 1)
            
        # Adding that removed element to the front of the list
        nums.insert(0, number_to_remove)


        