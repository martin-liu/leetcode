import unittest
from typing import List

class Solution(unittest.TestCase):
    def findMin(self, nums: List[int]) -> int:
        """
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2]
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
"""
        def find(start, end):
            if start >= end - 1:
                return min(nums[start], nums[end])
            if nums[start] < nums[end]:
                return nums[start]

            mid = (start + end) // 2
            return min(find(start, mid), find(mid+1, end))

        return find(0, len(nums)-1)

    def testFindMin(self):
        self.assertEqual(1, self.findMin([3,4,5,1,2]))
        self.assertEqual(0, self.findMin([4,5,6,7,0,1,2]))
