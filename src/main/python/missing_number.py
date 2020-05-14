import unittest
from typing import List

class Solution(unittest.TestCase):
    def missingNumber(self, nums: List[int]) -> int:
        """
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

---
Basic idea: sum of subtract of i+1 - nums[i]
"""
        n = 0
        for i in range(len(nums)):
            n += i + 1 - nums[i]
        return n

    def testMissing(self):
        self.assertEqual(2, self.missingNumber([3,0,1]))
        self.assertEqual(8, self.missingNumber([9,6,4,2,3,5,7,0,1]))
