import unittest
from typing import List

class Solution(unittest.TestCase):
    def rob(self, nums: List[int]) -> int:
        """
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.

---
Basic Idea: DP.
        result: amount
        state: house (i), rob (0, 1)
        choice: rob or not
"""
        if not nums:
            return 0
        l = len(nums)
        dp = [[0, 0] for _ in range(l)]
        for i in range(l):
            if i == 0:
                dp[i][0] = 0
                dp[i][1] = nums[i]
            else:
                dp[i][0] = max(dp[i-1][0], dp[i-1][1])
                dp[i][1] = dp[i-1][0] + nums[i]

        return max(dp[l-1][0], dp[l-1][1])


    def testRob(self):
        self.assertEqual(4, self.rob([1,2,3,1]))
        self.assertEqual(12, self.rob([2,7,9,3,1]))
