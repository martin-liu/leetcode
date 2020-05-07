import unittest
from typing import List

class Solution(unittest.TestCase):
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        """
The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.



Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

---
Basic Idea: DP from right bottom -> left top, because needed HP is determined by next step, means netx step need to calculate first.

state: position (x, y)
choice: left or top
result: min HP
"""
        rows = len(dungeon)
        cols = len(dungeon[0])

        dp = [[[0] for _ in range(cols)] for _ in range(rows)]

        for i in range(rows-1, -1, -1):
            for j in range(cols-1, -1, -1):
                if i == rows-1 and j == cols-1:
                    dp[i][j] = max(1, 1 - dungeon[i][j])
                else:
                    bottom = dp[i+1][j] if i < rows-1 else dp[i][j+1]
                    right = dp[i][j+1] if j < cols-1 else dp[i+1][j]
                    minNeed = min(bottom, right)

                    # at least 1 in each position
                    dp[i][j] = max(1, minNeed - dungeon[i][j])
        return dp[0][0]

    def testDungeon(self):
        self.assertEqual(3, self.calculateMinimumHP([
            [1,-3,3],
            [0,-2,0],
            [-3,-3,-3]
        ]))
        self.assertEqual(7, self.calculateMinimumHP([
            [-2, -3, 3],
            [-5, -10, 1],
            [10, 30, -5],
        ]))
