import unittest

class Solution(unittest.TestCase):
    def uniquePaths(self, m: int, n: int) -> int:
        """
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3

Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

Example 2:

Input: m = 7, n = 3
Output: 28

        """
        if m <= 0 or n <= 0:
            return 0
        if m == 1 or n == 1:
            return 1

        nums = [[-1 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    nums[i][j] = 1
                else:
                    nums[i][j] = nums[i-1][j] + nums[i][j-1]

        return nums[m-1][n-1]

    def testUniquePaths(self):
        self.assertEqual(self.uniquePaths(3, 2), 3)
        self.assertEqual(self.uniquePaths(7, 3), 28)
