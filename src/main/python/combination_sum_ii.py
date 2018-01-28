"""
https://leetcode.com/problems/combination-sum-ii/description/

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
"""

# Basic idea: sort, then recursively generate combination
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
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

# -----------------------------
import unittest

class Test(unittest.TestCase):
    def test(self):
        s = Solution()

        self.assertEqual(s.combinationSum2([1, 2], 2), [[2]])
        self.assertEqual(s.combinationSum2([2, 3, 6, 7], 7), [[7]])
        self.assertEqual(s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8), sorted([
            [1, 7],
            [1, 2, 5],
            [2, 6],
            [1, 1, 6]
        ]))
