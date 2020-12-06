import unittest
from typing import List, Dict
from queue import Queue
from collections import defaultdict
from heapq import heappush, heappop

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
Basic idea: essentially shortest path of Graph, use Dijkstra
"""
        def dijkstra(graph: Dict[int, Dict[int, int]], s: int):
            """
            graph: dict of dict, e.g. {'A': {'B': 1, 'C': 2}}
            """
            parent = {s: None}
            distance = defaultdict(lambda: float('inf'))
            distance[s] = 0
            visited = set()
            pq = [(0, s)]

            while pq:
                dis, node = heappop(pq)
                # mark visited when pop the node, not like typical BFS, which mark visited before push to queue
                # this is because whe pop order will change with heap
                visited.add(node)

                for adj, adj_dis in graph[node].items():
                    dist = dis + adj_dis
                    # only when found shorter distance
                    if adj not in visited and dist < distance[adj]:
                        # update distance with shorter one
                        distance[adj] = dist
                        # track shorter adj for each node
                        parent[adj] = node
                        # choose shorter adj to move, with pq, shortest one will pop
                        heappush(pq, (dist, adj))

            return parent, distance

        graph = {n:{} for n in range(1,N+1)}
        for u,v,w in times:
            graph[u][v] = w

        _, distance = dijkstra(graph, K)

        return max(distance.values()) if len(distance.keys()) == N else -1

    def networkDelayTime2(self, times: List[List[int]], N: int, K: int) -> int:
        """
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
        self.assertEqual(2, self.networkDelayTime2([[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2))
