# Link to Problem: https://leetcode.com/problems/intersection-of-two-arrays-ii/
# Difficulty - Medium

# Leetcode Problem number 189: Intersection of two Arrays II - Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
    length_of_nums1 = len(nums1)
    length_of_nums2 = len(nums2)
        
    nums_answer =[]
        
    if length_of_nums1 < length_of_nums2:
            
        for number in nums1:
            if number in nums2:
                nums_answer.append(number)
                nums2.remove(number)
                    
    else: 
            
        for number in nums2:
            if number in nums1:
                nums_answer.append(number)
                nums1.remove(number)
                    
    return nums_answer