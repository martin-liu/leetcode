import unittest
from typing import List

class Solution(unittest.TestCase):
    def getRow(self, rowIndex: int) -> List[int]:
        """

Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?
"""
        if rowIndex < 0:
            return []
        row = []
        # rowIndex starts with 0, it needs `rowIndex+1` rounds
        for i in range(rowIndex+1):
            row.append(1)
            # i-1 until 1, since first/last is 1
            for j in range(i-1, 0, -1):
                row[j] = row[j] + row[j-1]
        return row

    def testRow(self):
        self.assertEqual([1,3,3,1], self.getRow(3))
        self.assertEqual([1,4,6,4,1], self.getRow(4))
        self.assertEqual([1,5,10,10,5,1], self.getRow(5))
