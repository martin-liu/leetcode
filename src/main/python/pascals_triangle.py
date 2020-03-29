import unittest
from typing import List

class Solution(unittest.TestCase):
    def generate(self, numRows: int) -> List[List[int]]:
        """
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

"""
        if numRows < 1:
            return []
        ret = [[1]]
        for i in range(1, numRows):
            ar = []
            for j in range(i+1):
                if j == 0 or j == i:
                    ar.append(1)
                else:
                    ar.append(ret[i-1][j-1] + ret[i-1][j])
            ret.append(ar)
        return ret

    def testPascal(self):
        self.assertEqual([[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]], self.generate(5))
