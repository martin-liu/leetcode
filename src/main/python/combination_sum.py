"""
Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:
[
  [7],
  [2, 2, 3]
]
"""

# Basic idea: sort first (so that can easily filter out bigger numbers), then recursively generate combination
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        if not candidates:
            return []

        candidates.sort()

        return self.generateCombination(candidates, target)

    def generateCombination(self, ar, target):
        if not ar:
            return []

        head = ar[0]
        tail = ar[1:]
        ret = []

        if head > target:
            # head greater than target, means no number less than target
            return []
        elif target % head == 0:
            # remainder is 0, means head can combine to target
            ret.append([head] * (target // head))

        # no matter head matches or not, check rest of array
        for i in range(target // head):
            # check target, target - head, target - head * 2, ...
            for c in self.generateCombination(tail, target - i * head):
                ret.append([head] * i + c)
        return ret


# -----------------------------
import unittest

class Test(unittest.TestCase):
    def test(self):
        s = Solution()

        self.assertEqual(s.combinationSum([1, 2], 2), [[1, 1], [2]])
        self.assertEqual(s.combinationSum([2, 3, 6, 7], 7), [[7], [2, 2, 3]])
