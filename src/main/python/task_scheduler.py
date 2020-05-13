import unittest
from typing import List
from collections import Counter

class Solution(unittest.TestCase):
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks. Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.



Example:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.


Constraints:

The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].

---
Basic Idea:
        M: count of the task that have biggest count
        Mcnt: how many task have count M (different task can have same count)

        When tasks can fill all intervals, result is `len(tasks)`
        When tasks cannot fill all intervals, result is max interval of max count one, i.e. `(M-1) * (n+1) + Mcnt`
"""
        if n == 0:
            return len(tasks)

        taskCnt = list(Counter(tasks).values())
        M = max(taskCnt)
        Mcnt = taskCnt.count(M)

        return max(len(tasks), (M-1) * (n+1) + Mcnt)

    def testLeast(self):
        self.assertEqual(8, self.leastInterval(["A","A","A","B","B","B"], 2))
        self.assertEqual(104, self.leastInterval(["A","A","A","B","B","B"], 50))
        self.assertEqual(9, self.leastInterval(["A","A","A","B","B","B","C","C","D"], 2))
