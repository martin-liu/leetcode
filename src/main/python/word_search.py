import unittest
from typing import List

class Solution(unittest.TestCase):
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
 ['A','B','C','E'],
 ['S','F','C','S'],
 ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

---
Basic idea: backtracking(DFS). Try each direction via `or`, so that if one direction matches, others will not execute.
        """
        if not board or not board[0] or not word:
            return False

        row = len(board)
        col = len(board[0])

        def travel(word, pos):
            if not word:
                return True
            x, y = pos
            if x < 0 or x >= row or y < 0 or y >= col or board[x][y] != word[0]:
                return False

            curr, rest = word[0], word[1:]
            # mark current position as empty, so that it will not be visited again
            board[x][y] = ''
            ret = travel(rest,(x+1,y)) or \
                travel(rest,(x,y+1)) or \
                travel(rest,(x,y-1)) or \
                travel(rest,(x-1,y))
            # reset current position, so that it will not impact other rounds
            board[x][y] = curr
            return ret

        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    if travel(word, (i,j)):
                        return True
        return False

    def testExist(self):
        board = [['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E']]
        self.assertTrue(self.exist(board, "ABCCED"))
        self.assertTrue(self.exist(board, "SEE"))
        self.assertFalse(self.exist(board, "ABCB"))
        self.assertFalse(self.exist(board, "AZCB"))

        board = [["C","A","A"],["A","A","A"],["B","C","D"]]
        self.assertTrue(self.exist(board, "AAB"))
