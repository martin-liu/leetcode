import unittest
from typing import List

class Solution(unittest.TestCase):
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
 [2],
 [1],
 [1,2,2],
 [2,2],
 [1,2],
 []
]

---
Basic idea: f([first, *rest]) = f(rest) + [[first] + a for a in f(rest)], only need to deal with duplication
        """
        def doSubsets(nums):
            if not nums:
                return [[]]
            rest = doSubsets(nums[1:])
            ret = [[nums[0]] + a for a in rest]
            for d in rest:
                if d not in ret:
                    ret = [d] + ret
            return ret
        return doSubsets(sorted(nums))

    def testSubsetsWithDup(self):
        self.assertCountEqual(self.subsetsWithDup([1,2,2]), [[2], [1], [1,2,2], [2,2], [1,2], []])
        self.assertCountEqual(self.subsetsWithDup([4,4,4,1,4]), [[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]])
