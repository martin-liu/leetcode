import unittest
from typing import List

class Solution(unittest.TestCase):
    def generateMatrix(self, n: int) -> List[List[int]]:
        """
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

---

Basic idea:
        """
        if n == 0:
            return []
        elif n == 1:
            return [[1]]

        ret = [[-1 for i in range(n)] for j in range(n)]

        x, y = 0, 0
        dx, dy = 0, 1 # direction
        minRow, maxRow = 0, n - 1
        minCol, maxCol = 0, n - 1

        for i in range(1, n * n + 1):
            ret[x][y] = i

            rotate = False
            if dx == 1 and x == maxRow:
                maxCol -= 1
                rotate = True
            elif dx == -1 and x == minRow:
                minCol += 1
                rotate = True
            elif dy == 1 and y == maxCol:
                minRow += 1
                rotate = True
            elif dy == -1 and y == minCol:
                maxRow -= 1
                rotate = True

            if rotate:
                dx, dy = dy, -dx

            x, y = x + dx, y + dy

        return ret

    def testGenerateMatrix(self):
        self.assertCountEqual(self.generateMatrix(0), [])
        self.assertCountEqual(self.generateMatrix(1), [[1]])
        self.assertCountEqual(
            self.generateMatrix(2),
            [[ 1, 2 ],
             [ 4, 3 ]]
        )

        self.assertCountEqual(
            self.generateMatrix(3),
            [[ 1, 2, 3 ],
             [ 8, 9, 4 ],
             [ 7, 6, 5 ]]
        )
