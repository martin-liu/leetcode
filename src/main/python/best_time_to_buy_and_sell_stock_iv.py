import unittest
from typing import List

class Solution(unittest.TestCase):
    def maxProfit(self, k: int, prices: List[int]) -> int:
        """
Say you have an array for which the i-th element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example 1:

Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
        """
        if k < 1 or not prices:
            return 0

        if k > (len(prices) // 2):
            # means can use any time of buy/sell
            k = len(prices) // 2
            profits = [[0] * 2 for _ in range(len(prices))]
            for i in range(len(prices)):
                if i == 0:
                    profits[i][0] = 0
                    profits[i][1] = - prices[i]
                else:
                    # previsous day have no stock in hand, or have stock and sell today
                    profits[i][0] = max(profits[i-1][0], profits[i-1][1] + prices[i])
                    # previsous day have stock in hand, or no stock and buy today
                    profits[i][1] = max(profits[i-1][1], profits[i-1][0] - prices[i])
            return profits[len(prices)-1][0]

        profits = [[[0] * 2 for _ in range(k+1)] for _ in range(len(prices))]
        for i in range(len(prices)):
            for j in range(k+1):
                if i == 0:
                    profits[i][j][0] = 0
                    profits[i][j][1] = - prices[i]
                elif j == 0:
                    profits[i][j][0] = 0
                else:
                    # previsous day have no stock in hand, or have stock and sell today
                    profits[i][j][0] = max(profits[i-1][j][0], profits[i-1][j][1] + prices[i])
                    # previsous day have stock in hand, or no stock and buy today
                    profits[i][j][1] = max(profits[i-1][j][1], profits[i-1][j-1][0] - prices[i])
        return profits[len(prices)-1][k][0]

    def testMaxProfit(self):
        self.assertEqual(2, self.maxProfit(2, [2,4,1]))
        self.assertEqual(7, self.maxProfit(2, [3,2,6,5,0,3]))
        self.assertEqual(7, self.maxProfit(200, [3,2,6,5,0,3]))
