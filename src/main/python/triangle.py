import unittest
from typing import List

class Solution(unittest.TestCase):
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
"""
        nums = [[0] * (i+1) for i in range(len(triangle))]
        for i in range(len(triangle)):
            for j in range(i+1):
                if i == 0 and j == 0:
                    nums[i][j] = triangle[i][j]
                else:
                    preL = nums[i-1][j-1] if j > 0 else nums[i-1][j]
                    preR = nums[i-1][j] if j < i else nums[i-1][j-1]
                    nums[i][j] = min(preL, preR) + triangle[i][j]
        return min(nums[-1])

    def minimumTotal2(self, triangle: List[List[int]]) -> int:
        if not triangle or not triangle[0]:
            return 0
        ret = float('inf')
        def backtrack(track):
            nonlocal ret
            if len(track) == len(triangle):
                ret = min(ret, sum(map(lambda d:d[1], track)))
            else:
                for i, n in enumerate(triangle[len(track)]):
                    index = track[-1][0] if len(track) > 0 else 0
                    if i == index or i == index + 1:
                        backtrack(track + [(i, n)])
        backtrack([])
        return ret

    def testMin(self):
       self.assertEqual(11, self.minimumTotal([[2], [3,4], [6,5,7], [4,1,8,3]]))
       self.assertEqual(-1, self.minimumTotal([[-1],[2,3],[1,-1,-3]]))
