import unittest
from typing import List

class Solution(unittest.TestCase):
    def solve(self, board: List[List[str]]) -> None:
        """
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.


Basic idea: find all boarder 'O', from them to mark all connected 'O', them change all those not marked to `X`
"""
        if not board or not board[0] or len(board) <= 2 or len(board[0]) <= 2:
            return
        rows = len(board)
        cols = len(board[0])
        # point -> keep or not
        oMap = {}

        def surroundO(x, y):
            ret = []
            for i in [x-1, x, x+1]:
                for j in [y-1, y, y+1]:
                    if i >= 0 and i < rows and j >= 0 and j < cols and (i == x or j == y) and board[i][j] == 'O':
                        ret.append((i,j))
            return ret

        for i in range(rows):
            for j in range(cols):
                if board[i][j]=='O':
                    if (i,j) not in oMap:
                        oMap[(i,j)] = False
                    if i == 0 or j == 0 or i == rows-1 or j == cols-1:
                        oMap[(i,j)] = True
                        points = [(i,j)]

                        # can also use recursive dfs
                        while points:
                            newPoints = []
                            for x,y in points:
                                for k, s in surroundO(x, y):
                                    if not oMap.get((k, s)):
                                        newPoints.append((k, s))
                                        oMap[(k, s)] = True
                            points = newPoints

        for (i,j), v in oMap.items():
            if not v:
                board[i][j] = 'X'

    def testSurroundRegions(self):
        board = [
            ["O","X","X","O","X"],
            ["X","O","O","X","O"],
            ["X","O","X","O","X"],
            ["O","X","O","O","O"],
            ["X","X","O","X","O"]
        ]

        self.solve(board)
        self.assertEqual(board, [
            ["O","X","X","O","X"],
            ["X","X","X","X","O"],
            ["X","X","X","O","X"],
            ["O","X","O","O","O"],
            ["X","X","O","X","O"]
        ])


        board = [
            ['X','X','X','X'],
            ['X','O','O','X'],
            ['X','X','O','X'],
            ['X','O','X','X']
        ]

        self.solve(board)
        self.assertEqual(board, [
            ['X','X','X','X'],
            ['X','X','X','X'],
            ['X','X','X','X'],
            ['X','O','X','X']
        ])
