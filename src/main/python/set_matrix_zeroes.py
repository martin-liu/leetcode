import unittest
from typing import List

class Solution(unittest.TestCase):
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input:
[
 [1,1,1],
 [1,0,1],
 [1,1,1]
]
Output:
[
 [1,0,1],
 [0,0,0],
 [1,0,1]
]

Example 2:

Input:
[
 [0,1,2,0],
 [3,4,5,2],
 [1,3,1,5]
]
Output:
[
 [0,0,0,0],
 [0,4,5,0],
 [0,3,1,0]
]

Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

---
Basic idea: 2 pass. use first row and first column to store state, then iterate from bottom right (so that will not set first row/colmn and impact others) and set zero
        O(1) space
        """
        if not matrix or not matrix[0]:
            return

        row = len(matrix)
        col = len(matrix[0])

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(row-1,-1,-1):
            for j in range(col-1,-1,-1):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

    def testSetZeros(self):
        mx = [[1,1,1], [1,0,1], [1,1,1]]
        self.setZeroes(mx)
        self.assertCountEqual(mx, [[1,0,1], [0,0,0], [1,0,1]])

        mx = [[0,1,2,0], [3,4,5,2], [1,3,1,5]]
        self.setZeroes(mx)
        self.assertCountEqual(mx, [[0,0,0,0], [0,4,5,0], [0,3,1,0]])
