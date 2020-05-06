import unittest
from typing import List

class Solution(unittest.TestCase):
    def majorityElement(self, nums: List[int]) -> int:
        """
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""

        need = len(nums) // 2 + 1
        counter = {}
        for n in nums:
            if n not in counter:
                counter[n] = 1
            else:
                counter[n] += 1
                if counter[n] >= need:
                    return n

    def testMajority(self):
        self.assertEqual(3, self.majorityElement([3,2,3]))
        self.assertEqual(2, self.majorityElement([2,2,1,1,1,2,2]))
