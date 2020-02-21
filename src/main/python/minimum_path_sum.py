import unittest
from typing import List

class Solution(unittest.TestCase):
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
 [1,3,1],
 [1,5,1],
 [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.

---
Basic idea: DP
        """
        if not grid or not grid[0]:
            return 0

        row = len(grid)
        col = len(grid[0])
        sums = [[0 for _ in range(col)] for _ in range(row)]

        for i in range(row):
            for j in range(col):
                ar = []
                if i > 0:
                    ar.append(sums[i-1][j])
                if j > 0:
                    ar.append(sums[i][j-1])

                sums[i][j] = min(ar or [0]) + grid[i][j]

        return sums[row-1][col-1]

    def testMinPathSum(self):
        self.assertEqual(self.minPathSum([]), 0)
        self.assertEqual(self.minPathSum([[3]]), 3)
        self.assertEqual(self.minPathSum([[1,3,1],[1,5,1],[4,2,1]]), 7)
