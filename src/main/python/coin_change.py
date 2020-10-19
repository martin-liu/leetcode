import unittest
from typing import List

class Solution(unittest.TestCase):
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.

----
Basic Idea: DP. `f(c, n) = min([f(c,n-c1), f(c, n-c2), ...]) + 1`
        State: current coin; amount
        Choice: use or not
        Transform: for each coin, dp[n] = min(dp[n], dp[n-coin] + 1)
"""
        INF = float('inf')
        dp = [0] + [INF] * amount
        for n in range(1, amount+1):
            for coin in coins:
                dp[n] = min(dp[n], dp[n-coin] + 1 if n >= coin else INF)
        return dp[amount] if dp[amount] != INF else -1

    def test(self):
        self.assertEqual(0, self.coinChange([2], 0))
        self.assertEqual(-1, self.coinChange([], 3))
        self.assertEqual(-1, self.coinChange([2], 3))
        self.assertEqual(4, self.coinChange([2], 8))
        self.assertEqual(3, self.coinChange([1,2,5], 11))
        self.assertEqual(25, self.coinChange([3,7,405,436], 8839))
