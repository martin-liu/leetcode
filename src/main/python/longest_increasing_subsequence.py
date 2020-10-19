import unittest
from typing import List

class Solution(unittest.TestCase):
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?

---
Basic Idea: DP.
        State: current index
        Output: LIS which end is current num
        Choice: compare all previous LIS, choose longest one that end is current num
"""
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp or [0]) # [0] for empty nums

    def test(self):
        self.assertEqual(0, self.lengthOfLIS([]))
        self.assertEqual(1, self.lengthOfLIS([12]))
        self.assertEqual(4, self.lengthOfLIS([10,9,2,5,3,7,101,18]))
