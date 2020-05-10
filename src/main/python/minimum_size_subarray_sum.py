import unittest
from typing import List

class Solution(unittest.TestCase):
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        """
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example:

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).
"""
        if not len(nums):
            return 0

        l, r = 0, 0
        minLen, sumN = float('inf'), 0
        while r < len(nums):
            sumN += nums[r]
            r += 1
            while sumN >= s:
                minLen = min(minLen, r-l)
                sumN -= nums[l]
                l += 1
        return minLen if minLen != float('inf') else 0

    def testMinSub(self):
        self.assertEqual(2, self.minSubArrayLen(7, [2,3,1,2,4,3]))
        self.assertEqual(0, self.minSubArrayLen(7, [2,3]))
