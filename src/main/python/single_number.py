import unittest
from typing import List

class Solution(unittest.TestCase):
    def singleNumber(self, nums: List[int]) -> int:
        """
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4

---
Basic Idea: same number xor itself will be 0, do xor for all the nums, the final result will be the single one
"""
        ret = None
        for n in nums:
            if ret is None:
                ret = n
            else:
                ret ^= n

        return ret


    def testSingleNumber(self):
        self.assertEqual(1, self.singleNumber([2,2,1]))
        self.assertEqual(4, self.singleNumber([4,1,2,1,2]))
