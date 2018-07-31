"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

[
  [7,8,9],
  [4,5,6],
  [1,2,3]
]
rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
"""

# Basic idea: reverse matrix, then swap matrix[i][j] and matrix[j][i]
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        n = len(matrix)
        for i in range(0, n):
            for j in range(i + 1, n):
                t = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = t

    # rotate manually
    def rotate2(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        if not matrix or len(matrix) == 1:
            return

        length = len(matrix)
        start = 0
        end = length - 1

        while start < end:
            # rotate outer rect
            for i in range(start, end):
                tmp = matrix[start][i]
                matrix[start][i] = matrix[start + end - i][start]
                matrix[start + end - i][start] = matrix[end][start + end - i]
                matrix[end][start + end - i] = matrix[i][end]
                matrix[i][end] = tmp
            # rotate inner matrix
            start += 1
            end -= 1



# -----------------------------
import unittest

class Test(unittest.TestCase):
    def test(self):
        s = Solution()

        matrix = [[1]]
        s.rotate(matrix)
        self.assertEqual(matrix, [[1]])


        matrix = [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]

        s.rotate(matrix)
        self.assertEqual(matrix, [
            [7,4,1],
            [8,5,2],
            [9,6,3]
        ])


        matrix = [
            [ 5, 1, 9,11],
            [ 2, 4, 8,10],
            [13, 3, 6, 7],
            [15,14,12,16]
        ]

        s.rotate(matrix)
        self.assertEqual(matrix, [
            [15,13, 2, 5],
            [14, 3, 4, 1],
            [12, 6, 8, 9],
            [16, 7,10,11]
        ])
