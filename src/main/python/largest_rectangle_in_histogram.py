import unittest
from typing import List

class Solution(unittest.TestCase):
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10 unit.

Example:

Input: [2,1,5,6,2,3]
Output: 10

---
Basic idea: lagest rectangle depends on smallest height in a range. So for each height x, check the range that x is smallest.
Use a Monotonic stack to only push index when meet bigger, and pop when meet smaller. So that when pop, `heights[stack[-1]] < heights[poppedIndex] < heights[i]`, the largestRectangleArea of poppedIndex will be `heights[poppedIndex] * (i - stack[-1] -1)`
        """
        if not heights:
            return 0

        # add 2 sentries to make logic simpler/cleaner
        # first sentry is used to avoid index out bound
        # second sentry is used to clear stack to ensure all the bars are checked/calculated
        heights = [-1] + heights + [-1]
        ret = 0
        stack = []
        for i, h in enumerate(heights):
            # for every h, check the range that h is smallest
            while stack and h < heights[stack[-1]]:
                # check until h is not smallest
                ret = max(ret, heights[stack.pop()] * (i - stack[-1] - 1))
            # append every index of h, so that we keep data in stack in small
            # -> big order that means, every `popped height index` will have
            # `heights[stack[-1]] < heights[poped index] < heights[i]`
            stack.append(i)
        return ret

    def testLargestRectangleArea(self):
        self.assertEqual(self.largestRectangleArea([]), 0)
        self.assertEqual(self.largestRectangleArea([2]), 2)
        self.assertEqual(self.largestRectangleArea([0,2]), 2)
        self.assertEqual(self.largestRectangleArea([1,2,3]), 4)
        self.assertEqual(self.largestRectangleArea([2,1,5,6,2,3]), 10)
