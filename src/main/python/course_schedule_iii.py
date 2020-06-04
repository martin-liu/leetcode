import unittest
from typing import List
from heapq import heappush, heappop

class Solution(unittest.TestCase):
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        """
There are n different online courses numbered from 1 to n. Each course has some duration(course length) t and closed on dth day. A course should be taken continuously for t days and must be finished before or on the dth day. You will start at the 1st day.

Given n online courses represented by pairs (t,d), your task is to find the maximal number of courses that can be taken.

Example:

Input: [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
          100, 100    1100, 200     250, 1000    1200, 2000
Output: 3
Explanation:
There're totally 4 courses, but you can take 3 courses at most:
First, take the 1st course, it costs 100 days so you will finish it on the 100th day, and ready to take the next course on the 101st day.
Second, take the 3rd course, it costs 1000 days so you will finish it on the 1100th day, and ready to take the next course on the 1101st day.
Third, take the 2nd course, it costs 200 days so you will finish it on the 1300th day.
The 4th course cannot be taken now, since you will finish it on the 3300th day, which exceeds the closed date.


Note:

The integer 1 <= d, t, n <= 10,000.
You can't take two courses simultaneously.

---
Basic Idea: Greedy, local optimal: shortest total time in biggest range.
        Sort by end time, so that when iterating, we always have bigger range. (means we can safely remove any existing one without worry end date)
        Use max heap to store time, when total time not enough, pop the longest one, so that we have shortest total time
"""
        # sort by end date
        courses.sort(key=lambda c: c[1])
        total, heap = 0, []
        for c in courses:
            t, d = c
            total += t
            heappush(heap, -t)
            # when no enough time, pop the longest one that we added.
            # because the end time of longest one <= current one, so that we have shortest time in biggest range
            if total > d:
                total += heappop(heap)

        return len(heap)

    def test(self):
        self.assertEqual(5, self.scheduleCourse([[5,15],[3,19],[6,7],[2,10],[5,16],[8,14],[10,11],[2,19]]))
        self.assertEqual(2, self.scheduleCourse([[5,5],[4,6],[2,6]]))
        self.assertEqual(4, self.scheduleCourse([[2,5],[2,19],[1,8],[1,3]]))
        self.assertEqual(3, self.scheduleCourse([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]))
        self.assertEqual(2, self.scheduleCourse([[100, 200], [250, 1300], [1000, 1250]]))
