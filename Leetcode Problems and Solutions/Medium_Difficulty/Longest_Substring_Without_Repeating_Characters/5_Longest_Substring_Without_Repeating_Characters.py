# Link to Problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Difficulty - Medium

# Leetcode Problem number 5: Longest Substring without repeating characters: Given a string s, find the length of the longest substring without repeating characters.


from typing import List, Tuple, Dict
import timeit


# A single pass O(N) solution worked using the `sliding window` algorithmic approach
def lengthOfLongestSubstringUsingSets(s: str) -> int:

    myset = set()

    left_pointer = 0
    right_pointer = 0

    max_len = 0

    while(right_pointer < len(s)):

        if s[right_pointer] not in myset:


            myset.add(s[right_pointer])
            right_pointer += 1
            max_len = max(max_len, len(myset))
        
        else:
            myset.discard(s[left_pointer])
            left_pointer += 1

    return max_len

def lengthOfLongestSubstringUsingDictonary(s: str) -> int:

    myDict = {}
    max_len = 0

    left_pointer = 0
    

    for right_pointer in range(len(s)):

        if s[right_pointer] not in myDict:

            myDict[s[right_pointer]] = right_pointer
            max_len = max(max_len, right_pointer - left_pointer + 1)
        
        else: 
            left_pointer = max(left_pointer, myDict[s[right_pointer]] + 1)
            
    return max_len

def checkDuplicates(s: str) -> bool:
        
    input_dict = {}
    for char in s:
        if char not in input_dict:
            input_dict[char] = 1
        else:
            input_dict[char] += 1
        
    for key in input_dict:
        if input_dict[key] > 1:
            return True
        
    return False

# Brute force solution which doesnt get accepted by Leetcode Judge due to time limit exceeded 
def lengthOfLongestSubstringBruteForce(s: str) -> int:
        
    if len(s) == 0:
        return 0
        
    max_length = 0
        
    for i in range(len(s)):
        for j in range(len(s) - 1, i, -1):
            substringConsidered = s[i: j + 1]
                
            if not checkDuplicates(substringConsidered):
                max_length = max(max_length, len(substringConsidered))
        
    if max_length == 0:
        return 1

    return max_length
    
# Testing

input_string = "abcbabcbb"

start_time = timeit.default_timer()

print(lengthOfLongestSubstringUsingDictonary(input_string))
stop_time = timeit.default_timer()

diff = stop_time - start_time

print(f"The time taken is: {diff}")

# print(len(input_string))