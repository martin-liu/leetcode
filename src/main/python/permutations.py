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
"""

# Basic idea: each round, insert n to each position of each array
class Solution(object):
    def permute(self, nums):
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
            ret = ls
        return ret



# -----------------------------
import unittest

class Test(unittest.TestCase):
    def test(self):
        s = Solution()

        ar = [
            [1,2,3],
            [1,3,2],
            [2,1,3],
            [2,3,1],
            [3,1,2],
            [3,2,1]
        ]

        self.assertEqual(sorted(s.permute([1,2,3])), sorted(ar))
