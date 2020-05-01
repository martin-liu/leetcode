import unittest
from typing import List
from collections import defaultdict
from fractions import Fraction

class Solution(unittest.TestCase):
    def maxPoints(self, points: List[List[int]]) -> int:
        """
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Example 1:

Input: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o
+------------->
0  1  2  3  4
Example 2:

Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.


"""
        if not points or not points[0]:
            return 0
        if len(points) in [1, 2]:
            return len(points)

        lines = defaultdict(set)
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                if x1 == x2:
                    a, b = x1, None
                elif y1 == y2:
                    a, b = None, y1
                else:
                    # use Fraction to prevent float number precision issue (another way is use gcd to generate fraction like key)
                    a = Fraction(y2 - y1, x2 - x1)
                    b = y2 - a * x2
                lines[(a, b)].add(i)
                lines[(a, b)].add(j)
        _, line = max(lines.items(), key=lambda d: len(d[1]))
        return len(line)

    def testMax(self):
        self.assertEqual(3, self.maxPoints([[1,1],[2,2],[3,3]]))
        self.assertEqual(4, self.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))
