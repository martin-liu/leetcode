import unittest
from typing import List
from heapq import heappush, heappop

class Solution(unittest.TestCase):
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.

---
Basic Idea: K-Way Merge, use min heap, first push first one of each row, then pop smallest one, push next one in same row as smallest one. Repeat until finish/meet.
"""
        L = len(matrix)
        heap = []
        for i in range(L):
            heappush(heap, (matrix[i][0], i, 0))

        res = None
        while k > 0:
            # pop smallest one
            res, x, y = heappop(heap)
            k -= 1
            if y < L-1:
                # next to smallest one can be next smallest, add to heap to compare
                heappush(heap, (matrix[x][y+1], x, y+1))

        return res

    def test(self):
        self.assertEqual(13, self.kthSmallest(matrix = [[ 1,  5,  9], [10, 11, 13], [12, 13, 15]], k = 8))
