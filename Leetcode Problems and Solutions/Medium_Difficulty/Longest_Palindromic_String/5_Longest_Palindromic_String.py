# Link to Problem: https://leetcode.com/problems/longest-palindromic-substring/
# Difficulty - Medium

# Leetcode Problem number 5: Two Sum - Given a string s, return the longest palindromic substring in s.

# A O(N^2) solution to longest palindromic substring, in which we consider each character as a midpoint and `expand` towards the left and right, finding palindromes this way

# A helper function to find out all palindromic substrings by expanding from the centre of the string 's' 
def expandFromCenter(s: str, fromLeft: int, fromRight: int) -> str:

    while fromLeft >= 0 and fromRight < len(s) and s[fromLeft] == s[fromRight]:
        fromLeft -= 1
        fromRight += 1
    
    return s[fromLeft + 1: fromRight]

def longestPalindrome(s: str) -> str:

    # A variable to hold the longest palindromic substring found so far
    longestPalindromicSubstring = ""

    # A variable to hold the length of the longest palindromic substring found so far
    lengthOfLongestPalindromicSubstring = 0
   
   # We consider each character of the input string as the midpoint and `expand` in both directions to find the longest palindromic substring
    for i in range(len(s)):

       # Case 1: We have an odd numbered palindromic substring. For this we consider s[i] as the midpoint and expand from there on
        substringConsidered = expandFromCenter(s, i, i)
        print(f"substring from odd: {substringConsidered}")
        lengthOfSubstringConsidered = len(substringConsidered)

       # See if the substring we found is the longest or not, by updating palindromic substring
        if lengthOfSubstringConsidered > lengthOfLongestPalindromicSubstring:
            longestPalindromicSubstring = substringConsidered
            lengthOfLongestPalindromicSubstring = lengthOfSubstringConsidered
        
        # Case 2: We have to consider all even numbered palindromic substrings. In this case we have two midpoints, s[i] and the adjacent character s[i + 1] to expand from in both the directions, going towards the left from s[i] and towards the right from s[i + 1]
        print("odd line break")
        substringConsidered = expandFromCenter(s, i, i + 1)
        print(f"substring from even: {substringConsidered}")
        lengthOfSubstringConsidered = len(substringConsidered)

        # See if the even numbered palindrome is longest or not and if so, update it
        if lengthOfSubstringConsidered > lengthOfLongestPalindromicSubstring:
            longestPalindromicSubstring = substringConsidered
            lengthOfLongestPalindromicSubstring = lengthOfSubstringConsidered
        
        
    return longestPalindromicSubstring


# A brute force solution to the longest Palindromic substring - O(N^3) solution which is not accepted
def longestPalindromeBruteForceSolution(s: str) -> str:

    # Checking base cases
    if len(s) < 2:
            return s
        
    if len(s) == 2: 
        if s == s[::-1]:
            return s
            
        return s[0]
    
    # When the length of the input string is > 2
    result = ""

    # Looping through to find all possible substrings
    for i in range(len(s)):
        for j in range(len(s) - 1, i, -1):

            # Checking if the substring is a palindrome
            if s[i: j + 1] == s[i: j + 1][::-1]:

                # Finding the longest substring out of all the palindromic substrings   
                if len(s[i: j + 1]) > len(result):
                    result = s[i: j + 1]

    if result == "":
        return s[0]

    return result

# Test-cases to test functionality

input_string = "cbbd"
print(longestPalindrome(input_string))