import unittest
from typing import List
from queue import Queue
from collections import defaultdict

class Solution(unittest.TestCase):
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        """
There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.

Example 1:

Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
Output: 2

Note:

N will be in the range [1, 100].
K will be in the range [1, N].
The length of times will be in the range [1, 6000].
All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 0 <= w <= 100.

---
Basic idea: BFS, track total time to each node, use min time when node visited multiple times
"""
        # all node cannot be reached at beginning
        T = [0] + [float('inf')] * N
        G = defaultdict(lambda:[])
        for u, v, w in times:
            G[u].append((v,w))

        q = Queue()
        q.put((K, 0))

        while not q.empty():
            u, time = q.get()

            # min time to node u
            if time < T[u]:
                T[u] = time

                # only continue when current is min
                for v, w in G[u]:
                    q.put((v, time+w))

        return max(T) if max(T) != float('inf') else -1

    def test(self):
        self.assertEqual(2, self.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2))
