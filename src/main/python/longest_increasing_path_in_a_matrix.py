import unittest
from typing import List

class Solution(unittest.TestCase):
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

Input: nums =
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].

Example 2:

Input: nums =
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

---
Basic Idea: DP. f(pos) means longest length which start at position pos, this need position with bigger numbers to calculate first.
        One trick to reduce dimention from 2D to 1D is using complex number, i.e. `x + y*1j`, and dict
"""
        matrix = {x + y * 1j: val
                  for x, row in enumerate(matrix)
                  for y, val in enumerate(row)}

        lengths = {}
        # sort by value desc
        # because to make DP works for increasing path, bigger ones need to calculate first
        for z in sorted(matrix, key=matrix.get, reverse=True):
            lengths[z] = 1 + max([lengths[Z]
                                 for Z in [z+1, z-1, z+1j, z-1j]
                                 if Z in matrix and matrix[z] < matrix[Z]]
                                or [0])

        return max(lengths.values() or [0])

    def test(self):
        self.assertEqual(4, self.longestIncreasingPath([[9,9,4], [6,6,8], [2,1,1]]))
        self.assertEqual(4, self.longestIncreasingPath([[3,4,5], [3,2,6], [2,2,1]]))
