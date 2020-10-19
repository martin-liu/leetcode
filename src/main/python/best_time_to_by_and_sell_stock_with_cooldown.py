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
