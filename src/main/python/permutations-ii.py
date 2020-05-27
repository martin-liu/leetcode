import unittest
from collections import Counter

class Solution(unittest.TestCase):
    def permuteUnique(self, nums):
        """
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
---
Basic Idea: Backtracking, use a counter to determine choices (count > 0)
"""
        res, L = [], len(nums)
        def backtrack(path, counter):
            if len(path) == L:
                res.append(path)
            else:
                for n in counter:
                    if counter[n] > 0:
                        counter[n] -= 1
                        # duplicated ones still have counter[n] > 0
                        backtrack(path + [n], counter)
                        counter[n] += 1
        backtrack([], Counter(nums))
        return res

    def permuteUnique2(self, nums):
        if not nums:
            return []

        ret = [[]]
        for n in nums:
            ls = []
            for ar in ret:
                for i in range(len(ar) + 1):
                    ls.append(ar[:i] + [n] + ar[i:])
                    # process duplicates
                    # because ret is symmetrical, so that when `n == ar[i]`, no need to continue; and in other `ar`, it will cover what we ignored in this round
                    # e.g. ar = [ [1, 2], [2, 1] ], n = 1, => [ [1, 1, 2], [1, 2, 1], [2, 1, 1] ]
                    if i < len(ar) and ar[i] == n:
                        break
            ret = ls
        return ret

    def test(self):
        self.assertCountEqual(self.permuteUnique([1,1,2]), [
            [1,1,2],
            [1,2,1],
            [2,1,1]
        ])
