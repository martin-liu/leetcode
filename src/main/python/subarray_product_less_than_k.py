import unittest
from typing import List

class Solution(unittest.TestCase):
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """
Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:

Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Note:

0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6.

---
Basic Idea: Sliding window, count add `r-l+1` when r add 1
"""
        if k == 0:
            return 0
        l, r = 0, 0
        prod = 1
        ret = 0
        while r < len(nums):
            prod *= nums[r]
            while l <= r and prod >= k:
                prod /= nums[l]
                l += 1
            ret += r-l+1
            r += 1
        return ret


    def testProductLessThanK(self):
        self.assertEqual(8, self.numSubarrayProductLessThanK([10,5,2,6], 100))
