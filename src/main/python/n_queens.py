import unittest
from typing import List

class Solution(unittest.TestCase):
    def solveNQueens(self, n) -> List[List[str]]:
        """
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
"""
        if n <= 0:
            return []
        res = []
        def backtrack(path):
            L = len(path)
            if L == n:
                queen = ["".join(['Q' if i == p else '.' for i in range(n)]) for p in path]
                res.append(queen)
            else:
                for i in range(n):
                    # no same column and same cross line
                    if i not in path and all(abs(L-x) != abs(i-y) for x, y in enumerate(path)):
                        backtrack(path + [i])

        backtrack([])
        return res

    def solveNQueens2(self, n):
        ret = []
        for queens in self.doNQueens(n, n):
            board = [['.'] * n for _ in range(n)]
            for queen in queens:
                board[queen[0] - 1][queen[1] - 1] = 'Q'
                board[queen[0] - 1] = "".join(board[queen[0] - 1])
            ret.append(board)
        return ret

    def doNQueens(self, n, k):
        if k == 0:
            return [[]]
        else:
            ret = []
            preNQueens = self.doNQueens(n, k - 1)
            for queens in preNQueens:
                for i in range(1, n + 1):
                    queen = (k, i)
                    if self.isValid(queen, queens):
                        ret.append(queens + [queen])
            return ret

    def isValid(self, queen, queens):
        return all(self.isSafe(queen, q) for q in queens)

    def isSafe(self, queen1, queen2):
        return not (
            queen1[0] == queen2[0] or  # same row
            queen1[1] == queen2[1] or  # same column
            abs(queen2[0] - queen1[0]) == abs(queen2[1] - queen1[1])  # cross
        )

####----------Solution 2-----------#####

    def solveNQueens3(self, n):
        res = []
        def dfs(rows, diag, r_diag, res, n):
            if len(rows) == n:
                res.append(rows)
                return
            n_r = len(rows)
            for i in range(n):
                if i not in rows and (n_r + i) not in r_diag and (n_r - i) not in diag:
                    dfs(rows+[i], diag+[n_r - i], r_diag+[n_r + i], res, n)

        dfs([], [], [], res, n)
        return [['.'* i + 'Q' + '.'*(n-i-1) for i in sol] for sol in res]

    def test(self):
        self.assertEqual(self.solveNQueens(1), [['Q']])
        self.assertEqual(self.solveNQueens(2), [])
        self.assertEqual(self.solveNQueens(4), [['.Q..', '...Q', 'Q...', '..Q.'], ['..Q.', 'Q...', '...Q', '.Q..']])
