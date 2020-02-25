import unittest
from typing import List

class Solution(unittest.TestCase):
    def search(self, nums: List[int], target: int) -> bool:
        """
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
Follow up:

This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?

---
Basic idea: binary search, check if `mid < end`
        """
        if not nums:
            return False
        elif len(nums) == 1:
            return nums[0] == target

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (r+l) // 2
            if nums[mid] == target:
                return True
            elif l == r:
                return False

            if nums[mid] < nums[r]:
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            elif nums[mid] > nums[r]:
                if target <= nums[mid] and target > nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                # mid == end, cannot determine, do fallback move
                r -= 1

        return False

    def testSearch(self):
        #self.assertFalse(self.search([1,3], 2))
        self.assertTrue(self.search([1,3], 3))
        self.assertTrue(self.search([2,5,6,0,0,1,2], 0))
        self.assertFalse(self.search([2,5,6,0,0,1,2], 3))
