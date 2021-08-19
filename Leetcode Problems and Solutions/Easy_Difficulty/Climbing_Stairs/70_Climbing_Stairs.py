# Link to problem: https://leetcode.com/problems/climbing-stairs/
# Difficulty level: Easy

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

def climbStairs(n: int) -> int:
            # Base cases
        if n == 1:
            return 1
        
        if n == 2:
            return 2
        
        # For all inputs n >= 3, we use dynammic programming
        
        # Initialising the dp_array. dp[i] is the number of steps needed to reach the (i  + 1)th step
        dp_array = [0] * n
        
        # There is one way to reach the first step
        dp_array[0] = 1
        
        # There are two ways to reach the second step
        dp_array[1] = 2
        
        '''
        For n >= 3(From the third step onwards), we can either reach it from the (n -1)th
        step and then take one step, or go to the (n - 2)th step and take 2 steps to reach
        the nth step
        '''
        for i in range(2, n):
            dp_array[i] = dp_array[i - 1] + dp_array[i - 2]
        
        # As with any dp problem, the answer is the last element of the dp_array
        return dp_array[-1]

# Testing

n = 44

print(climbStairs(n))