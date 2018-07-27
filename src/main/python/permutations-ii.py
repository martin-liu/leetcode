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
"""

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

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




# -----------------------------
import unittest

class Test(unittest.TestCase):
    def test(self):
        s = Solution()

        self.assertEqual(sorted(s.permuteUnique([1,1,2])), sorted([
            [1,1,2],
            [1,2,1],
            [2,1,1]
        ]))
