import unittest
from typing import List

class Solution(unittest.TestCase):
    def canPartition(self, nums: List[int]) -> bool:
        """
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.

Constraints:
1 <= nums.length <= 200
1 <= nums[i] <= 100

---
Basic Idea: DP. Essentially find any sum equal to sum/2.
        base case: False
        state: num index, sum that can got
        choice: prefix index, sum - n
        def: dp[i][j] = dp[i-1][j] || dp[i-1][j-nums[i]]
"""
        S = sum(nums)
        if not nums or S & 1 == 1:
            return False

        # target sum/2
        S = S//2
        dp = [False] * (S+1)
        dp[0] = True

        for n in nums:
            for i in range(S, 0, -1):
                if i >= n:
                    # if dp[i-n] already meet, means dp[i] meet
                    dp[i] = dp[i] or dp[i-n]
        return dp[S]

    def canPartition2(self, nums: List[int]) -> bool:
        """
        transform: f(i, s) = f(i-1, |s-nums[i]|) or f(i-1, |s+nums[i]|)
        """
        cache = {}
        def can(i: int, s: int) -> bool:
            if (i,s) in cache:
                return cache[(i,s)]

            res = False
            if i == 0:
                res = nums[i] == s
            elif i > 0:
                res = can(i-1, abs(s+nums[i])) or can(i-1, abs(s-nums[i]))

            cache[(i,s)] = res
            return res

        return can(len(nums)-1, 0)

    def test(self):
        self.assertFalse(self.canPartition([]))
        self.assertTrue(self.canPartition([1,5,11,5]))
        self.assertTrue(self.canPartition([5,11,5,1]))
        self.assertTrue(self.canPartition([2,1,4,3]))
        self.assertTrue(self.canPartition([4,1,3]))
        self.assertFalse(self.canPartition([1,2,3,5]))
