import unittest
from typing import List

class Solution(unittest.TestCase):
    def rob(self, nums: List[int]) -> int:
        """
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

----
Basic Idea: DP. Do 2 times, check rob first case, and not rob first case
        State: house number; robbed or not
        Choice: rob or not
"""
        L = len(nums)
        if L < 3:
            return max(nums or [0])

        dp = [[0, 0] for _ in range(L)]
        # case 1: rob first one
        for i in range(L):
            if i == 0:
                dp[i][0] = -float('inf')
                dp[i][1] = nums[i]
            else:
                dp[i][0] = max(dp[i-1][0],dp[i-1][1])
                dp[i][1] = dp[i-1][0] + nums[i]

        # when rob first, last one will not rob, so only choose dp[-1][0]
        res = dp[-1][0]

        # case 2: don't rob first one
        for i in range(L):
            if i == 0:
                dp[i][0] = 0
                dp[i][1] = -float('inf')
            else:
                dp[i][0] = max(dp[i-1][0],dp[i-1][1])
                dp[i][1] = dp[i-1][0] + nums[i]

        # when not rob first, last one can rob but may not rob
        return max(res, dp[-1][0], dp[-1][1])

    def test(self):
        self.assertEqual(self.rob([]), 0)
        self.assertEqual(self.rob([1]), 1)
        self.assertEqual(self.rob([2,3,2]), 3)
        self.assertEqual(self.rob([1,2,3,1]), 4)
