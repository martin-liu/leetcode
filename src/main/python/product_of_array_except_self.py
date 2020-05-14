import unittest
from typing import List

class Solution(unittest.TestCase):
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

---
Basic Idea: 2 pass, calculate product before that number, then calculate product after that number
"""
        res = []
        prod = 1
        for i in range(len(nums)):
            res.append(prod)
            prod *= nums[i]

        prod = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= prod
            prod *= nums[i]

        return res

    def testProduct(self):
        self.assertEqual([24,12,8,6], self.productExceptSelf([1,2,3,4]))
