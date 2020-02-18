import unittest
from typing import List

class Solution(unittest.TestCase):
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

---

Basic idea: use 2 array to store left and right intervals, build overlap interval and concat all
        """
        if not intervals:
            return [newInterval] if newInterval else []

        left, right = [], []
        l, r = newInterval

        for il, ir in intervals:
            if il > r:
                right.append([il, ir])
            elif ir < l:
                left.append([il, ir])
            else:
                l, r = min(l, il), max(r, ir)

        return left + [[l, r]] + right

    def testInsert(self):
        self.assertCountEqual(self.insert([], []), [])
        self.assertCountEqual(self.insert([], [5,7]), [[5,7]])
        self.assertCountEqual(self.insert([[1,5]], [2,3]), [[1,5]])
        self.assertCountEqual(self.insert([[1,3],[6,9]], [0,5]), [[0,5],[6,9]])
        self.assertCountEqual(self.insert([[2,5],[6,7],[8,9]], [0,1]), [[0,1],[2,5],[6,7],[8,9]])
        self.assertCountEqual(self.insert([[1,3],[4,5],[6,9]], [1,9]), [[1,9]])
        self.assertCountEqual(self.insert([[1,3],[6,9]], [2,5]), [[1,5],[6,9]])
        self.assertCountEqual(self.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]), [[1,2],[3,10],[12,16]])
