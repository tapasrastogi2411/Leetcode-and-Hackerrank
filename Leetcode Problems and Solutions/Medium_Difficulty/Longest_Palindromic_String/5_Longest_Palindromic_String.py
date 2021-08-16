# Link to Problem: https://leetcode.com/problems/longest-palindromic-substring/
# Difficulty - Medium

# Leetcode Problem number 5: Two Sum - Given a string s, return the longest palindromic substring in s.

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

# input_string = "okfzopfdxngrcukpqwmgyfbwzkqegoglsqszdihswhcnwaajuiagxscrwoicsdvyowbowaddignjgsjrhhhookusgnykutrkpogmvruwdkpjucslsoluhnooysjichvobriksbanovvynfwtooygdtflnchtgcycjiziytrhsomevozdxxbiwiuxrhxtyefogphgavlhbvdjpcosexyrmphcyuhqymnzkngqyitzekwimveydjrxkhvhckqcjetpmhxzisdlkhmotwcgejllzdmfwrbpzuxcawgamamkziewwqnxpvyhvmzulivwrngrsnarsmeunbpbnnvvlxllvniskaerpawflwfdozfsmovvjtymsgnvmfepidyffwjxpvpgwceukgfplqcyccejatqqmefquirgztnyawkruasuitnjldxgmmqzzvwltetjyenbicgabtnkpfdcanggcensptcgyyygnkbvcgmvzichisofakajqtsfogqewegawcjtylxavxdxdznzyxyvvupnwfxogyjmbayeminbzthyidymnmuoevrgfbdpodbdrznmosuispnmimrglgrkdrdsjmyacfmuntvgpjaginmyknawgonibhifpyhqoswyefidrtsqgwqviseayzxqwgelgtnvxlrdhpnuhxhianiqjiyygagwwmyklszbyhcykhejijhnfmrsagsbfthmzmzractm"

input_string = "abcda"

print(longestPalindromeBruteForceSolution(input_string))



    # lengthOfString = len(s)
    
    # # To capture the start and end of the substring we find
    # startIndex = 0
    # endIndex = 0

    # # Lengths, one for even numbered palindrome substring and another for the odd numbered palindrome substring
    # lengthOfEven = 0
    # lengthOfOdd = 0
    # lengthOfMax = 0

    # # Base Case
    # if lengthOfString < 2:
    #     return s
    
    # # Traversing through the string
    # for i in range(lengthOfString):

    #     # For odd numbered palindromic substrings
    #     lengthOfOdd = expandAroundCenter(s, i, i) 

    #     # For even numbered palindromic substrings
    #     lengthOfEven = expandAroundCenter(s, i, i + 1)

    #     # Choose the max of the two choices we have
    #     lengthOfMax = max(lengthOfOdd, lengthOfEven)

    #     if lengthOfMax > endIndex - startIndex:

    #         # Update end and start index

   
