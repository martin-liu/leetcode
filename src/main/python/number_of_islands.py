import unittest
from typing import List
from queue import Queue

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
