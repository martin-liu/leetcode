import unittest
from typing import List
from queue import Queue

class UF(object):
    def __init__(self, n):
        self.count = n
        self.parent = [i for i in range(n)]

    def union(self, p, q):
        rp = self.find(p)
        rq = self.find(q)
        if rp == rq:
            return
        self.parent[rp] = rq
        self.count -= 1

    def find(self, p):
        while self.parent[p] != p:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

class Solution(unittest.TestCase):
    def numIslands(self, grid: List[List[str]]) -> int:
        """
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
----
Basic Idea: Union Find, connect all zero with a virtual root, then connect 1 to adj 1, count - 1 will be island number
"""
        if not grid or not grid[0]:
            return 0
        row, col = len(grid), len(grid[0])
        n = row * col # 2d to 1d
        uf = UF(n+1) # last one is virtual root for zeroes

        def adj(x,y):
            surround = []
            if x > 0:
                surround.append((x-1,y))
            if x < row-1:
                surround.append((x+1,y))
            if y > 0:
                surround.append((x,y-1))
            if y < col-1:
                surround.append((x,y+1))
            return [p for p in surround if grid[p[0]][p[1]] != '0']

        for i in range(row):
            for j in range(col):
                # projection in 1d
                x = i * col + j
                if grid[i][j] == '0':
                    # connect to virtual root
                    uf.union(x, n)
                else:
                    for p in adj(i,j):
                        uf.union(x, p[0] * col + p[1])
                    grid[i][j] = '0'

        return uf.count - 1

    def numIslands2(self, grid: List[List[str]]) -> int:
        """
---
Basic Idea: for each `1`, BFS to find all surround `1`, mark them to `X`. Those `1` without any `X` around count 1 island.
"""
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        queue = Queue()
        visited = {}

        ret = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    queue.put((i,j))
                    while not queue.empty():
                        x, y = queue.get()
                        surround = []
                        if x > 0:
                            surround.append((x-1,y))
                        if x < rows-1:
                            surround.append((x+1,y))
                        if y > 0:
                            surround.append((x,y-1))
                        if y < cols-1:
                            surround.append((x,y+1))

                        grid[x][y] = 'X'
                        valid = True
                        for x, y in surround:
                            valid &= grid[x][y] != 'X'
                            if grid[x][y] == '1' and (x,y) not in visited:
                                queue.put((x,y))
                                visited[(x,y)] = True
                        if valid:
                            ret += 1

        return ret

    def testNum(self):
        self.assertEqual(1, self.numIslands([
            ['1','1','1','1','0'],
            ['1','1','0','1','0'],
            ['1','1','0','0','0'],
            ['0','0','0','0','0'],
        ]))
        self.assertEqual(3, self.numIslands([
            ['1','1','0','0','0'],
            ['1','1','0','0','0'],
            ['0','0','1','0','0'],
            ['0','0','0','1','1'],
        ]))
        self.assertEqual(1, self.numIslands([["1","1","1"],["0","1","0"],["1","1","1"]]))
        self.assertEqual(1, self.numIslands([
            ["1","0","1","1","1"],
            ["1","0","1","0","1"],
            ["1","1","1","0","1"]]))
