import unittest
from typing import List

class Solution(unittest.TestCase):
    def sortedSquares(self, A: List[int]) -> List[int]:
        """
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]


Note:

1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A is sorted in non-decreasing order.
"""
        if not A:
            return []

        L = len(A)
        l, r, i = 0, L-1, L-1
        ret = [0] * L

        while l <= r:
            lSquare = A[l] * A[l]
            rSquare = A[r] * A[r]
            if lSquare > rSquare:
                ret[i] = lSquare
                l += 1
            else:
                ret[i] = rSquare
                r -= 1
            i -= 1

        return ret

    def testSortedSquares(self):
        self.assertEqual([0,1,9,16,100], self.sortedSquares([-4,-1,0,3,10]))
        self.assertEqual([4,9,9,49,121], self.sortedSquares([-7,-3,2,3,11]))
