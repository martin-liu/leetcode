import unittest
from typing import List

class Solution(unittest.TestCase):
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
There are a number of spherical balloons spread in two-dimensional space. For each balloon, provided input is the start and end coordinates of the horizontal diameter. Since it's horizontal, y-coordinates don't matter and hence the x-coordinates of start and end of the diameter suffice. Start is always smaller than end. There will be at most 104 balloons.

An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend. There is no limit to the number of arrows that can be shot. An arrow once shot keeps travelling up infinitely. The problem is to find the minimum number of arrows that must be shot to burst all balloons.

Example:

Input:
[[10,16], [2,8], [1,6], [7,12]]

Output:
2

Explanation:
One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).

"""
        if not points:
            return 0
        if len(points) == 1:
            return 1
        # sort by end
        points.sort(key=lambda d:d[0])

        length, i, j, res = len(points), 0, 1, 1
        while j < length:
            pre, curr = points[i], points[j]
            if pre[1] < curr[0]:
                # found new non-overlap one
                res += 1
                i = j
            j += 1

        return res

    def testArrow(self):
        self.assertEqual(2, self.findMinArrowShots([[10,16], [2,8], [1,6], [7,12]]))
