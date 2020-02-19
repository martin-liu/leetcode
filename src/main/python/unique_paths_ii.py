import unittest
from typing import List

class Solution(unittest.TestCase):
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2

Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
        """
        if not obstacleGrid or not obstacleGrid[0] or obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0

        row = len(obstacleGrid)
        col = len(obstacleGrid[0])

        paths = [[0 for _ in range(col)] for _ in range(row)]

        firstRowObstacle = None
        firstColObstacle = None
        for i in range(row):
            for j in range(col):
                if obstacleGrid[i][j] == 1:
                    paths[i][j] = 0
                    if not firstRowObstacle and i == 0:
                        firstRowObstacle = j
                    if not firstColObstacle and j == 0:
                        firstColObstacle = i
                elif i == 0 or j == 0:
                    if firstRowObstacle and i == 0 and j >= firstRowObstacle:
                        paths[i][j] = 0
                    elif firstColObstacle and j == 0 and i >= firstColObstacle:
                        paths[i][j] = 0
                    else:
                        paths[i][j] = 1
                else:
                    paths[i][j] = paths[i-1][j] + paths[i][j-1]

        return paths[row-1][col-1]

    def testUniqPath(self):
        self.assertEqual(self.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]), 2)
        self.assertEqual(self.uniquePathsWithObstacles(
            [[0,0],[1,1],[0,0]]), 0)
