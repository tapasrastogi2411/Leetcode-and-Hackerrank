# Link to Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Difficulty - Easy

# Leetcode Problem number 121: You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

from typing import List, Tuple, Dict

# importing the module
import timeit
  

def maxProfit(prices: List[int]) -> int:
    
    # An array to store the profit to get the maximum profit from
    profit_array = []
    # Start the first iteration of the list
    for buy_price_index in range(len(prices)):
        buy_price_to_consider = prices[buy_price_index]
        for sell_price_index in range(buy_price_index + 1, len(prices)):
            # Use prices[buy_price_index] and prices[sell_price_index] to get profit in each case

            profit = prices[sell_price_index] - prices[buy_price_index]
            profit_array.append(profit)
        
    if max(profit_array) <= 0:
        return 0
    
    return max(profit_array)
                
            

    pass

# Testing

input_prices = [10000,9999,9998,9997,9996,9995,9994,9993,9992,9991,9990,9989,9988,9987,9986,9985,9984,9983,9982,9981,9980]

print(maxProfit(input_prices))