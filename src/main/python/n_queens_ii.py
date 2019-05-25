"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example:

Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""

class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:return[]
        self.count = 0
        self.DFS(n, 0, 0, 0, 0)
        return self.count

    def DFS(self, n, row, cols, pie, na):
        if row >= n:
            self.count += 1
            return

        bits = (~(cols|pie|na))&((1<<n) - 1)

        while bits:
            p = bits & -bits
            self.DFS(n, row+1, cols|p, (pie|p)<<1, (na|p)>>1)
            bits = bits &(bits-1)

# -----------------------------
import unittest

class Test(unittest.TestCase):
    def test(self):
        s = Solution()

        self.assertEquals(s.totalNQueens(1), 1)
        self.assertEquals(s.totalNQueens(2), 0)
        self.assertEquals(s.totalNQueens(3), 0)
        self.assertEquals(s.totalNQueens(4), 2)
        self.assertEquals(s.totalNQueens(8), 92)
