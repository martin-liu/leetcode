import unittest
from typing import List

class Solution(unittest.TestCase):
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""
        res = []
        for n in nums:
            i = abs(n)-1
            if nums[i] < 0:
                res.append(i+1)
            else:
                nums[i] = - nums[i]

        return res

    def testDuplicate(self):
        self.assertEqual([2,3], self.findDuplicates([4,3,2,7,8,2,3,1]))
