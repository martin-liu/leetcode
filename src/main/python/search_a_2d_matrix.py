import unittest
from typing import List

class Solution(unittest.TestCase):
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
 [1,   3,  5,  7],
 [10, 11, 16, 20],
 [23, 30, 34, 50]
]
target = 3
Output: true

Example 2:

Input:
matrix = [
 [1,   3,  5,  7],
 [10, 11, 16, 20],
 [23, 30, 34, 50]
]
target = 13
Output: false
        """

        if not matrix or not matrix[0]:
            return False

        row = len(matrix)
        col = len(matrix[0])

        length = row * col
        start, end = 0, length - 1
        while start <= end:
            mid = (start+end)//2
            q, r = divmod(mid, col)
            if matrix[q][r] == target:
                return True
            elif matrix[q][r] < target:
                start = mid + 1
            else:
                end = mid - 1
        return False

    def testSearchMatrix(self):
        matrix = [[1,   3,  5,  7], [10, 11, 16, 20], [23, 30, 34, 50]]
        self.assertTrue(self.searchMatrix(matrix, 3))
        self.assertFalse(self.searchMatrix(matrix, 13))
