# Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

# Note: You may not slant the container and n is at least 2.

# Basic idea: area determined by min height, from left & right to check
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ret = 0
        start = 0
        lenH = len(height)
        end = lenH - 1

        while start < end:
            minH = min(height[start], height[end])
            # area determined by min height
            area = minH * (end - start)
            ret = max(ret, area)

            # skip all height <= minH
            while start < lenH and height[start] <= minH:
                start += 1
            while end > 0 and height[end] <= minH:
                end -= 1
        return ret


# -----------------------------
import unittest

class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.maxArea([1, 2, 3]), 2)
        self.assertEqual(s.maxArea([1, 3, 5]), 3)
        self.assertEqual(s.maxArea([1, 3, 15, 55, 5]), 15)
