import unittest
from typing import List

class Solution(unittest.TestCase):
    def longestConsecutive(self, nums: List[int]) -> int:
        """
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

---
Basic Idea: if `n-1` not in nums, means n can be a start, check `n+1` until not find, count it
"""
        nums = set(nums)
        res = 0
        for n in nums:
            if n-1 not in nums:
                # n can be a start when n-1 not there
                end = n+1
                while end in nums:
                    end += 1
                res = max(res, end - n)
        return res

    def testLongestConsecutive(self):
        self.assertEqual(4, self.longestConsecutive([100,4,200,1,3,2]))
