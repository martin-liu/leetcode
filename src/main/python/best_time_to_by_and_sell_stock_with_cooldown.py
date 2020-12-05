import unittest
from typing import List

class Solution(unittest.TestCase):
    def maxProfit(self, prices: List[int]) -> int:
        """
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]

---
Basic Idea: DP.
        state: day `i`, how many transactions `k` (any k, means no need to care), hold or not hold stock `j`
        choice: buy, sell, rest
        definition:
          f(i, 0) = max( f(i-1,0), f(i-1, 1) + prices[i] )
          f(i, 1) = max( f(i-1,1), f(i-2, 0) - prices[i] )
"""
        L = len(prices)
        dp = [[0,0] for _ in range(len(prices))]
        for i, p in enumerate(prices):
            if i == 0:
                dp[i][1] = -p
            else:
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + p)
                dp[i][1] = max(dp[i-1][1], (dp[i-2][0] if i >= 2 else 0) - p)

        return max(dp[L-1][0], dp[L-1][1])

    def maxProfit2(self, prices: List[int]) -> int:
        """
Basic Idea: DP. State machine. s0 -buy-> s1 -sell-> s2 -rest-> s0
        s0[i] = max(s0[i - 1], s2[i - 1]); // Stay at s0, or rest from s2
        s1[i] = max(s1[i - 1], s0[i - 1] - prices[i]); // Stay at s1, or buy from s0
        s2[i] = s1[i - 1] + prices[i]; // Only one way from s1
"""
        L = len(prices)
        if L <= 1:
            return 0

        s0, s1, s2 = [0] * L, [0] * L, [0] * L
        s1[0] = -prices[0]
        s2[0] = -float('inf')

        for i in range(1, L):
            s0[i] = max(s0[i-1], s2[i-1])
            s1[i] = max(s1[i-1], s0[i-1] - prices[i])
            s2[i] = s1[i-1] + prices[i]

        return max(s0[-1], s2[-1])

    def test(self):
        self.assertEqual(3, self.maxProfit([1,2,3,0,2]))
        self.assertEqual(3, self.maxProfit2([1,2,3,0,2]))
