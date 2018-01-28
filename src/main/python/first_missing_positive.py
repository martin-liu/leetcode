"""
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
"""

# Basic idea: store all `0 < n <= length` to map, then check missing from 1
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1

        length = len(nums)
        m = {}
        for n in nums:
            # only need to care `0 < n <= length`, because out of this
            # range will never be first missing positive
            if n > 0 and n <= length:
                m[n] = True
        i = 1
        while i in m:
            i += 1

        return i


# -----------------------------
import unittest

class Test(unittest.TestCase):
    def test(self):
        s = Solution()

        self.assertEqual(s.firstMissingPositive([1, 2, 0]), 3)
        self.assertEqual(s.firstMissingPositive([3, 4, -1, 1]), 2)
        self.assertEqual(s.firstMissingPositive([1, 3, 9, 5, 2, 7, -1, 0, 10]), 4)
