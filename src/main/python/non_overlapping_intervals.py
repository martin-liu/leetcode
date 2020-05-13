import unittest
from typing import List

class Solution(unittest.TestCase):
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Example 1:
Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.

Example 2:
Input: [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.

Example 3:
Input: [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.


Note:

You may assume the interval's end point is always bigger than its start point.
Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.

---
Basic Idea: sort by end, greedy remove overlaps. Because less end will have less overlaps, keep less end one will eventually have less removes.
"""
        if not intervals or len(intervals) == 1:
            return 0

        # sort by end
        intervals.sort(key=lambda d: d[1])
        length, i, j = len(intervals), 0, 1
        res = 0
        while j < length:
            pre, curr = intervals[i], intervals[j]
            if curr[0] < pre[1]:
                # have overlap, remove it
                res += 1
            else:
                i = j
            j += 1
        return res

    def testErase(self):
        self.assertEqual(1, self.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
        self.assertEqual(2, self.eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
        self.assertEqual(0, self.eraseOverlapIntervals([[1,2],[2,3]]))
