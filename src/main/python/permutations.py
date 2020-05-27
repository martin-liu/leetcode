import unittest

class Solution(unittest.TestCase):
    def permute(self, nums):
        """
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
---
Basic idea: Backtracking
"""
        res, L = [], len(nums)
        def backtrack(path):
            if len(path) == L:
                res.append(path)
            else:
                for n in nums:
                    if n not in path:
                        backtrack(path + [n])
        backtrack([])
        return res

    def permute2(self, nums):
        """
        Basic idea: each round, insert n to each position of each array
        """
        if not nums:
            return []

        ret = [[]]
        for n in nums:
            ls = []
            for ar in ret:
                for i in range(len(ar) + 1):
                    ls.append(ar[:i] + [n] + ar[i:])
            ret = ls
        return ret

    def test(self):
        ar = [
            [1,2,3],
            [1,3,2],
            [2,1,3],
            [2,3,1],
            [3,1,2],
            [3,2,1]
        ]

        self.assertCountEqual(self.permute([1,2,3]), ar)
