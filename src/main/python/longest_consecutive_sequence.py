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

"""
        if not nums:
            return 0

        # n-1 -> visited
        trackMap = {n-1:False for n in nums}

        ret = 1 # at least have one
        for n in nums:
            if n in trackMap and trackMap[n]:
                continue
            l = 0
            sub = n
            while sub in trackMap:
                trackMap[n] = True
                l += 1
                sub -= 1
            ret = max(ret, l)
        return ret

    def testLongestConsecutive(self):
        self.assertEqual(4, self.longestConsecutive([100,4,200,1,3,2]))
