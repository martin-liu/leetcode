import unittest
from typing import List

class Solution(unittest.TestCase):
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

---

Basic idea: sort the array, then try to merge until not able to do
        """
        intervals = sorted(intervals, key=lambda d: d[0])
        ret = []
        for iv in intervals:
            if not ret or ret[-1][1] < iv[0]:
                ret.append(iv)
            else:
                ret[-1] = [ret[-1][0], max(ret[-1][1], iv[1])]

        return ret

    def testMerge(self):
        self.assertCountEqual(self.merge([]), [])
        self.assertCountEqual(self.merge([[1,2]]), [[1,2]])
        self.assertCountEqual(self.merge([[1,2],[4,5],[4,7]]), [[1,2],[4,7]])
        self.assertCountEqual(self.merge([[1,3],[2,6],[8,10],[15,18]]), [[1,6],[8,10],[15,18]])
        self.assertCountEqual(self.merge([[1,4],[4,5]]), [[1,5]])
        self.assertCountEqual(self.merge([[1,4],[0,4]]), [[0,4]])
        self.assertCountEqual(self.merge([[1,4],[0,0]]), [[0,0], [1, 4]])
