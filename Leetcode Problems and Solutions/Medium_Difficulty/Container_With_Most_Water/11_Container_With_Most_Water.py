# Link to Problem: https://leetcode.com/problems/container-with-most-water/
# Difficulty - Medium

# Leetcode Problem number 5: Container with most water - Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

from typing import List, Tuple, Dict

# Trying out a brute force o(N^2) solution, trying out each pair of lines and finding out which of those pairs gives the maximum area - DOESNT WORK SINCE TIME LIMIT IS EXCEEDED

# Note: Area for two lines i and j is calculated as (j - i) * min(height[i], height[j])

# j and i above are the index of the different element in the heights list and height[i] and height[j] are the values at those indices which is actual length of the line at indices i and j

# Which is the min(of the two vertical lines at indices j and i),, that is the shorter line is the length and (j - i) is the width]
def maxArea(height: List[int]) -> int:

    # To get the maximum area, define a max_area variable
    max_area = 0

    for i in range(len(height)):
        for j in range(i + 1, len(height)):

            # Getting the dimensions of the container
            width_of_container = j - i
            height_of_container = min(height[i], height[j])

            # Computing the area
            area = height_of_container * width_of_container

            if area > max_area:
                max_area = area
    
    return max_area
    

# Testing

input_height = [1,8,6,2,5,4,8,3,7]

print(maxArea(input_height))
