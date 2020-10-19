import unittest
from typing import List

class NumArray:
    """
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:

Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:

You may assume that the array does not change.
There are many calls to sumRange function.
"""

    def __init__(self, nums: List[int]):
        dp = []
        for n in nums:
            if not dp:
                dp.append(n)
            else:
                dp.append(dp[-1] + n)
        self.dp = dp

    def sumRange(self, i: int, j: int) -> int:
        return self.dp[j] if i == 0 else self.dp[j] - self.dp[i-1]

class Tests(unittest.TestCase):
    def test(self):
        nums = [-2, 0, 3, -5, 2, -1]
        na = NumArray(nums)
        self.assertEqual(1, na.sumRange(0, 2))
        self.assertEqual(-1, na.sumRange(2, 5))
        self.assertEqual(-3, na.sumRange(0, 5))
