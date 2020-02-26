import unittest

class Solution(unittest.TestCase):
    def climbStairs(self, n: int) -> int:
        """
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
        """
        if n < 1:
            return 0

        ways = [0] * n
        for i in range(n):
            if i == 0:
                ways[i] = 1
            elif i == 1:
                ways[i] = 2
            else:
                ways[i] = ways[i-2] + ways[i-1]
        return ways[n-1]

    def testClimbingStairs(self):
        self.assertEqual(self.climbStairs(3), 3)
        self.assertEqual(self.climbStairs(4), 5)
        self.assertEqual(self.climbStairs(5), 8)
        self.assertEqual(self.climbStairs(6), 13)
