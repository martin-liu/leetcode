import unittest
from typing import List

class Solution(unittest.TestCase):
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""
        d = {}
        for n in nums:
            if n not in d:
                d[n] = 1
            elif d[n] == 1:
                return True
        return False

    def testContains(self):
        self.assertTrue(self.containsDuplicate([1,2,3,1]))
        self.assertFalse(self.containsDuplicate([1,2,3,4]))
        self.assertTrue(self.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
