import unittest
from typing import List

class Solution(unittest.TestCase):
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        """
Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

Example 1:

Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

Note:

1 <= k <= len(nums) <= 16.
0 < nums[i] < 10000.

---
Basic Idea: DP with bit mask.
        base case: False
        state: bitmap which represent subset of nums, e.g. 5=101 means subset which have 1rd or 3rd num
        dp[i] represents sum of current subset
"""
        if not nums:
            return False
        S, L = sum(nums), len(nums)
        if S % k != 0:
            return False

        target = S // k
        dp = [-1] * (1 << L)
        dp[0] = 0
        # i is any combination of nums (bitmap, e.g. 101 means subset which have first and third num)
        for i in range(1 << L):
            # if -1, means invalid subset
            if dp[i] == -1:
                continue
            # still need `rem` for current total to meet target, it'll have k rounds,
            # % will ensure it only consider current round
            rem = target - (dp[i] % target)
            for j in range(L):
                # add nums[j] to current subset to get a new subset
                future = i | (1 << j)
                if i == future or dp[future] >= 0:
                    # current or already set
                    continue
                # only need rem, so nums[j] should <= rem, otherwise means current subset not valid
                if nums[j] > rem:
                    break
                # nums[j] is valid for future subset
                dp[future] = dp[i] + nums[j]

        # last one should count all the nums, so total sholud be sum(nums)=S, otherwise means not valid in the process
        return dp[-1] == S

    def test(self):
        self.assertTrue(self.canPartitionKSubsets(nums = [3, 2, 1], k = 2))
        #self.assertTrue(self.canPartitionKSubsets(nums = [4, 3, 2, 3, 5, 2, 1], k = 4))
