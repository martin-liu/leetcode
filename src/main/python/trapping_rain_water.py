"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
"""

class Solution(object):
    def trap(self, height):
        """
        Monotonic decreasing stack, only when meet a higher one, then need to calculate
        Calculation:
          When we have `pree > pre < curr`, we calculate interval [pree, pre, curr]
          M = min(pree, curr), water += (M-pre) * n
          Now it's kind like we filled the interval with [M,M,M] waters, next interval no need to consider it any more
        """
        if not height or len(height) == 1:
            return 0
        stack = []
        res = 0
        i = 0
        while i < len(height):
            if not stack or height[stack[-1]] >= height[i]:
                stack.append(i)
                i += 1
            else:
                pre = stack.pop()
                if stack:
                    # (min(pree, cur) - pre) * n
                    res += (min(height[stack[-1]], height[i]) - height[pre]) * (i - stack[-1] - 1)

        return res

    def trap2(self, height):
        """
        :type height: List[int]
        :rtype: int

 Basic idea: trap determine by the lower side, so that move & calculate from lower side (l or r), approaching to middle
 when meet bigger one, trap break and bigger one is new boundary
        """

        if not height:
            return 0

        length = len(height)
        trap = 0
        l, r = 0, length - 1
        maxL, maxR = 0, 0

        # approaching to middle, allow equal, because last move need calculate
        while l <= r:
            # move & calculate from the lower side
            if maxL < maxR:
                if height[l] > maxL:
                    # when greater than maxL, then invalid trap but be next boundary
                    maxL = height[l]
                else:
                    # when less than maxL, then valid trap
                    trap += maxL - height[l]
                l += 1
            else:
                if height[r] > maxR:
                    maxR = height[r]
                else:
                    trap += maxR - height[r]
                r -= 1

        return trap

# -----------------------------
import unittest

class Test(unittest.TestCase):
    def test(self):
        s = Solution()

        #self.assertEqual(s.trap([0, 2, 0]), 0)
        #self.assertEqual(s.trap([1, 7, 8]), 0)
        #self.assertEqual(s.trap([5,4,1,2]), 1)
        self.assertEqual(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]), 6)

        self.assertEqual(s.trap([5,2,1,2,1,5]), 14)
