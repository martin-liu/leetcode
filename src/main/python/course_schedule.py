import unittest
from typing import List
from queue import Queue

class Solution(unittest.TestCase):
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.


Constraints:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
1 <= numCourses <= 10^5

---
Basic Idea: BFS from roots, decrease indegree of child, then child's indegree is 0, means this child can be new parent
"""
        # parent -> children
        G = [[] for _ in range(numCourses)]
        # indegree of child
        degree = [0] * numCourses
        for child, parent in prerequisites:
            G[parent].append(child)
            degree[child] += 1

        # current root
        queue = Queue()
        for i in range(numCourses):
            if degree[i] == 0:
                queue.put(i)

        while not queue.empty():
            parent = queue.get()
            for child in G[parent]:
                degree[child] -= 1
                # 0 means all parent traveled
                if degree[child] == 0:
                    # make child as parent
                    queue.put(child)
        return all(i == 0 for i in degree)

    def test(self):
        self.assertTrue(self.canFinish(8, [[1,0],[2,6],[1,7],[6,4],[7,0],[0,5]]))
        self.assertTrue(self.canFinish(2, [[1,0]]))
        self.assertFalse(self.canFinish(2, [[1,0],[0,1]]))
