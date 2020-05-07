import unittest
import functools
from typing import List

class Solution(unittest.TestCase):
    def largestNumber(self, nums: List[int]) -> str:
        """
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an integer.

Basic Idea: Sort
        9 > 8xx
        3 < 34
        3 > 32
        32 > 321
        32 > 322 (32322 > 32232)
        32 < 323 (32323 < 32332)
        312 > 3122
        312 < 3123
"""
        nums = map(lambda d: str(d), nums)
        def cmp(a, b):
            pre, post = a+b, b+a
            if pre > post:
                return 1
            elif pre < post:
                return -1
            else:
                return 0

        nums = sorted(nums, reverse=True, key=functools.cmp_to_key(cmp))
        i = 0
        while i < len(nums)-1 and nums[i] == '0':
            i += 1
        return "".join(nums[i:])

    def testLargest(self):
        self.assertEqual("0", self.largestNumber([0,0]))
        self.assertEqual("210", self.largestNumber([10,2]))
        self.assertEqual("9534330", self.largestNumber([3,30,34,5,9]))
