import unittest
from typing import List

class Solution(unittest.TestCase):
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        """
Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)



Example 1:



Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Reminder: The inputs and the desired output are lists of Interval objects, and not arrays or lists.


Note:

0 <= A.length < 1000
0 <= B.length < 1000
0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9

---
Basic Idea: 2 pointers, move when have less right, because next left may still overlap.
        when ra >= rb, move in B; when ra <= rb, move in A
"""
        if not A or not B:
            return []
        lenA, lenB, i, j = len(A), len(B), 0, 0

        res = []
        while i < lenA and j < lenB:
            la, ra, lb, rb = A[i][0], A[i][1], B[j][0], B[j][1]
            if la <= lb <= ra or lb <= la <= rb:
                res.append([max(la, lb), min(ra, rb)])
            if ra >= rb:
                j += 1
            if ra <= rb:
                i += 1
        return res

    def testIntersection(self):
        self.assertEqual([[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]], self.intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]))
