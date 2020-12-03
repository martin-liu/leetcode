import unittest
from typing import List

class Solution(unittest.TestCase):
    def maxProduct(self, nums: List[int]) -> int:
        """
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

---
Basic Idea: DP. Either positive * positive, or negative * negative.
        Maintain subMax and subMin to check both case.
        subMax = max(subMax * n, n, subMin * n)
        subMin = min(subMin * n, n, subMax * n)
"""
        if not nums:
            return 0

        ret = subMax = subMin = nums[0]

        for i in range(1, len(nums)):
            n = nums[i]
            # need to use preMax since subMax will change in next line
            preMax = subMax
            # current max subarray
            subMax = max(subMax * n, n, subMin * n)
            # current min subarray
            subMin = min(subMin * n, n, preMax * n)
            ret = max(ret, subMax)
        return ret

    def testMax(self):
        self.assertEqual(6, self.maxProduct([2,3,-2,4]))
        self.assertEqual(0, self.maxProduct([-2,0,-1]))
        self.assertEqual(12, self.maxProduct([-4,-3,-2]))
        self.assertEqual(108, self.maxProduct([-1,-2,-9,-6]))
