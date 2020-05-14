import unittest

class Solution(unittest.TestCase):
    def firstMissingPositive(self, nums):
        """
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.

---
Basic idea: 3 pass. make n<=0 to L+1 (so that they'll not impact others), then use negative of nums[nums[i]] to indicate visited, find first nums[i]>0, result is i+1
        O(1) space
"""
        L = len(nums)
        for i in range(L):
            if nums[i] <= 0:
                nums[i] = L+1

        for i in range(L):
            index = abs(nums[i])-1
            if 0 <= index < L:
                nums[index] = - abs(nums[index])

        for i in range(L):
            if nums[i] > 0:
                return i + 1
        return L+1

    def test(self):
        self.assertEqual(self.firstMissingPositive([]), 1)
        self.assertEqual(self.firstMissingPositive([1,2,3]), 4)
        self.assertEqual(self.firstMissingPositive([0,1,2]), 3)
        self.assertEqual(self.firstMissingPositive([3,4,0,2]), 1)
        self.assertEqual(self.firstMissingPositive([1, 2, 0]), 3)
        self.assertEqual(self.firstMissingPositive([3, 4, -1, 1]), 2)
        self.assertEqual(self.firstMissingPositive([1, 3, 9, 5, 2, 7, -1, 0, 10]), 4)
