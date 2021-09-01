# Link to Problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Difficulty - Medium

# Leetcode Problem number 5: Longest Substring without repeating characters: Given a string s, find the length of the longest substring without repeating characters.


from typing import List, Tuple, Dict
import timeit


# A single pass O(N) solution worked using the `sliding window` algorithmic approach - using sets
def lengthOfLongestSubstringUsingSets(s: str) -> int:

    # Initialise a set to store the characters we encounter in the string
    myset = set()

    # The two pointers we need to create a `sliding window`
    left_pointer = 0
    right_pointer = 0

    # A variable to store the maximum length substring that we encounter
    max_len = 0

    # Our right_pointer is the variable that will go till the end of the input string
    while(right_pointer < len(s)):

        # If the character we are at in the string is not in the set, add it to the set, increment the right_pointer to move forward and get the maximum length of the substring encountered so far
        if s[right_pointer] not in myset:

            myset.add(s[right_pointer])
            right_pointer += 1
            max_len = max(max_len, len(myset))
        
        # If the character we are at is already in the set, then we start removing the elements from the set from the left, using the left pointer, shrinking the `window` and moving the left_pointer to the next element
        else:
            myset.discard(s[left_pointer])
            left_pointer += 1

    return max_len

# A solution to the problem using dictionaries/hashmap
def lengthOfLongestSubstringUsingDictonary(s: str) -> int:

    # This dictionary stores the characters it encounters as key and the latest place they were found in the string(their indices) as the corresponding values
    myDict = {}

    max_len = 0

    left_pointer = 0
    right_pointer = 0

    while right_pointer < len(s):
        '''
        If the character we are is already in the dictionary then we make the left pointer point to immediate
        next of the previous occurance of that character which is accesses through dict[s[right_pointer]].
         
        This is similar to moving the left_pointer by 1 and removing the element at the left_pointer in the `set`
        approach

        For the edge case of strings like "abba", we include the max() statement since at times, we only want to move 
        the position of the left_pointer if its the right thing to do, otherwise we leave it there
        '''
        if s[right_pointer] in myDict:

            left_pointer = max(left_pointer, myDict[s[right_pointer]] + 1)
        
        # Building up the dictionary and finding the maximum length substring. No `else` clause since the keys in the dictionary remain the same and are not modified as in the `set approach`
        myDict[s[right_pointer]] = right_pointer
        max_len = max(max_len, right_pointer - left_pointer + 1)
        right_pointer += 1
    
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

input_string = "tapasrastogi"

start_time = timeit.default_timer()

print(lengthOfLongestSubstringUsingDictonary(input_string))
