import unittest
from typing import List

class Solution(unittest.TestCase):
    def maxProfit(self, prices: List[int]) -> int:
        """
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

----
State: day(i), operation time(j), have or not have stock in hand (k=0/1)
Choice: buy, sell, none

state change:
        f(i,j,0) = max(f(i-1,j,0), f(i-1,j,1) + price)
        f(i,j,1) = max(f(i-1,j,1), f(i-1,j,0) - price)
limit on number of buying (since can sell only after buy)
        """
        if not prices:
            return 0

        profits = [[[0] * 2 for _ in range(3)] for _ in range(len(prices))]
        for i in range(len(prices)):
            for j in range(3):
                if i == 0:
                    profits[i][j][0] = 0
                    profits[i][j][1] = -prices[i]
                elif j == 0:
                    profits[i][j][0] = 0
                else:
                    # either no stock yesterday, or have stock yesterday and sell it today
                    profits[i][j][0] = max(profits[i-1][j][0], profits[i-1][j][1] + prices[i])
                    # either have stock yesterday, or no stock yesterday and buy it today. (`j-1` is we add limitation on buying, can only buy 2 times, can sell after buy)
                    profits[i][j][1] = max(profits[i-1][j][1], profits[i-1][j-1][0] - prices[i])

        return profits[len(prices)-1][2][0]

    def testMaxProfit(self):
        self.assertEqual(6, self.maxProfit([3,3,5,0,0,3,1,4]))
        self.assertEqual(4, self.maxProfit([1,2,3,4,5]))
        self.assertEqual(0, self.maxProfit([7,6,4,3,1]))
        self.assertEqual(7, self.maxProfit([6,1,3,2,4,7]))
        self.assertEqual(7, self.maxProfit([3,2,6,5,0,3]))
        self.assertEqual(13, self.maxProfit([1,2,4,2,5,7,2,4,9,0]))
