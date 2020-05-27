import unittest
from typing import List

class Solution(unittest.TestCase):
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
---
Basic Idea: Backtracking
"""
        res, L, candidates = [], len(candidates), sorted(candidates)
        def backtrack(path, start, t):
            if t == 0:
                if path not in res:
                    res.append(path)
            elif t > 0:
                for i in range(start, L):
                    backtrack(path + [candidates[i]], i+1, t-candidates[i])
        backtrack([], 0, target)
        return res

    def combinationSum2(self, candidates, target):
        """
        Basic idea: sort, then recursively generate combination
        """
        candidates.sort()

        return self.generateCombination(candidates, target)

    def generateCombination(self, ar, target):
        if not ar:
            return []

        ret = []
        head = ar[0]
        tail = ar[1:]

        if head > target:
            return []
        elif head == target:
            ret.append([head])
        else:
            for c in self.generateCombination(tail, target - head):
                ret.append([head] + c)

        # check rest of array anyway
        for c in self.generateCombination(tail, target):
            if c not in ret:
                ret.append(c)

        return ret

    def test(self):
        self.assertEqual(self.combinationSum2([1, 2], 2), [[2]])
        self.assertEqual(self.combinationSum2([2, 3, 6, 7], 7), [[7]])
        self.assertCountEqual(self.combinationSum([10, 1, 2, 7, 6, 1, 5], 8), [
            [1, 7],
            [1, 2, 5],
            [2, 6],
            [1, 1, 6]
        ])
