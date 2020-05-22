import unittest
from typing import List

class Solution(unittest.TestCase):
    def spiralOrder2(self, matrix: List[List[int]]) -> List[int]:
        """
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:

Input:
[
 [1, 2, 3, 4],
 [5, 6, 7, 8],
 [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

---

Basic idea: decide next move based on position and boundary
vector rotate 90 deg `(x,y) -> (y,-x)`: (0, 1) -> (1, 0) -> (0, -1) -> (-1, 0)
        """
        if not matrix or not matrix[0]:
            return []
        rowMax = len(matrix) - 1
        colMax = len(matrix[0]) - 1
        rowMin = 0
        colMin = 0

        x, y = 0, 0 # position
        dx, dy = 0, 1 # direction in axis
        ret = []

        while x >= rowMin and x <= rowMax and y >= colMin and y <= colMax:
            # add current position
            ret.append(matrix[x][y])

            # prepare next position
            if dx == 1 and x == rowMax:
                colMax -= 1
                rotate = True
            elif dy == 1 and y == colMax:
                rowMin += 1
                rotate = True
            elif dx == -1 and x == rowMin:
                colMin += 1
                rotate = True
            elif dy == -1 and y == colMin:
                rowMax -= 1
                rotate = True
            else:
                rotate = False

            if rotate:
                dx, dy = dy, -dx

            # move
            x, y = x + dx, y + dy

        return ret

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # pop first row, rotate matrix. zip([1,2],[3,4]) => [[1,3],[2,4]]
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])

    def testSprialOrder(self):
        self.assertEqual(self.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]), [1,2,3,6,9,8,7,4,5])
        self.assertEqual(self.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]), [1,2,3,4,8,12,11,10,9,5,6,7])
