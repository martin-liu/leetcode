import unittest
from typing import List

class Solution(unittest.TestCase):
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        """
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:

Input: nums is [1, 1, 1, 1, 1], S is 3.
Output: 5
Explanation:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
Note:

The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.

---
Basic Idea: DP
        state: i, currSum
        top to bottom
"""
        if not nums:
            return 0

        L = len(nums)
        cache = {}
        def dp(i, s):
            if i < 0:
                return 0
            elif i == 0 and (s == nums[i] or s == -nums[i]):
                # when n is 0, it can be both + and -
                return 1 if nums[i] != 0 else 2

            if (i,s) not in cache:
                cache[(i,s)] = dp(i-1, s + nums[i]) + dp(i-1, s - nums[i])
            return cache[(i,s)]

        return dp(L-1, S)

    def test(self):
        self.assertEqual(5, self.findTargetSumWays([1,1,1,1,1], 3))
        self.assertEqual(6184, self.findTargetSumWays([27,33,4,43,31,44,47,6,6,11,39,37,15,16,8,19,48,17,18,39], 24))
