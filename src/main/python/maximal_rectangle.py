import unittest
from typing import List

class Solution(unittest.TestCase):
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:

Input:
[
 ["1","0","1","0","0"],
 ["1","0","1","1","1"],
 ["1","1","1","1","1"],
 ["1","0","0","1","0"]
]
Output: 6

---
Basic idea: for each row, build a histogram of number of 1. Then for each row, use monotonic stack to calculate max.
e.g.
[['1','0']
 ['1','1']
 ['1','0']]
Will be
 [[1,0]
 [2,1]
 [3,0]]
       """
        if not matrix or not matrix[0]:
            return 0

        ret = 0
        curr = None
        for ar in matrix:
            ar = [int(d) for d in ar]
            if not curr:
                curr = ar
            else:
                # (x[0]+x[1])*x[1], so that if x[1] is 0, then 0, otherwise plus
                curr = [(x[0]+x[1])*x[1] for x in zip(curr, ar)]

            heights = [-1] + curr + [-1]
            stack = []
            for i, d in enumerate(heights):
                while stack and heights[stack[-1]] > d:
                    ret = max(ret, heights[stack.pop()] * (i - stack[-1] - 1))
                stack.append(i)

        return ret

    def testMaximalRectangle(self):
        self.assertEqual(self.maximalRectangle([]), 0)
        self.assertEqual(self.maximalRectangle([[]]), 0)
        self.assertEqual(self.maximalRectangle([[1], [1]]), 2)
        self.assertEqual(self.maximalRectangle([
            ["1","0","1","0","0"],
            ["1","0","1","1","1"],
            ["1","1","1","1","1"],
            ["1","0","0","1","0"]
        ]), 6)
