import unittest
from typing import List

class Solution(unittest.TestCase):
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
 [3],
 [1],
 [2],
 [1,2,3],
 [1,3],
 [2,3],
 [1,2],
 []
]

---
Basic idea: backtracking, for each subset end with nums[i], can append with any of nums[i+1] to nums[-1]
        """
        res, L = [], len(nums)
        def backtrack(index, path):
            res.append(path)
            # choices
            for i in range(index, L):
                backtrack(i+1, path + [nums[i]])

        backtrack(0, [])
        return res

    def subsets2(self, nums: List[int]) -> List[List[int]]:
        """
        Basic idea: f([first, *rest]) = f(rest) + [[first] + a for a in f(rest)]
        """
        if not nums:
            return [[]]
        rest = self.subsets2(nums[1:])
        return rest + [[nums[0]] + a for a in rest]

    def testSubsets(self):
        self.assertCountEqual(self.subsets([]), [[]])
        self.assertCountEqual(self.subsets([1]), [[1], []])
        self.assertCountEqual(self.subsets([1,2]), [[1], [2], [1,2], []])
        self.assertCountEqual(self.subsets([1,2,3]), [[3], [1], [2], [1,2,3], [1,3], [2,3], [1,2], []])
