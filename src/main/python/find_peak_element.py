import unittest
from typing import List

class Solution(unittest.TestCase):
    def findPeakElement(self, nums: List[int]) -> int:
        """
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5
Explanation: Your function can return either index number 1 where the peak element is 2,
             or index number 5 where the peak element is 6.
Note:

Your solution should be in logarithmic complexity.

"""
        if len(nums) == 1:
            return 0

        def find(l, r):
            if l > r:
                return None
            mid = (l+r)//2
            leftNum = nums[mid-1] if mid > 0 else -float('inf')
            rightNum = nums[mid+1] if mid < len(nums)-1 else -float('inf')
            if nums[mid] > leftNum and nums[mid] > rightNum:
                return mid
            elif r == l:
                return None

            left = find(l, mid-1)
            if left is not None:
                return left
            right = find(mid+1, r)
            if right is not None:
                return right

            return None
        return find(0, len(nums)-1)

    def testPeak(self):
        self.assertEqual(2, self.findPeakElement([1,2,3,1]))
        self.assertEqual(1, self.findPeakElement([1,2,1,3,5,6,4]))
        self.assertEqual(1, self.findPeakElement([1,2]))
        self.assertEqual(0, self.findPeakElement([2,1]))
