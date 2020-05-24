import unittest
from typing import List
from heapq import heappop, heappush

class Solution(unittest.TestCase):
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        """
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples:
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Your job is to output the median array for each window in the original array.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Median
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
Therefore, return the median sliding window as [1,-1,-1,3,5,6].

Note:
You may assume k is always valid, ie: k is always smaller than input array's size for non-empty array.
Answers within 10^-5 of the actual value will be accepted as correct.

---
Basic Idea: 2 heaps(min & max) with (n, i) as element. When out-of-window is not top of heap, then it will not impact median. [max...] < [min...]
        min/max heaps' size diff may greater than 1, because some element not popped.
"""
        if k == 1:
            return nums
        # for small(max heap), always do `-n` when push or pop, so that python's min heap implementation can represent max heap
        small, large = [], []

        def add(i):
            if nums[i] >= large[0][0]:
                heappush(large, (nums[i],i))
                # i-k is out of window, it will be removed.
                # if `i-k` in large, then we insert and remove one from large, no need to do any move.
                # if `i-k` in small, then we insert one to large, remove one from small. Now need to move one from large to small
                if i >= k and nums[i-k] <= large[0][0]:
                    move(large, small)
            else:
                heappush(small, (-nums[i], i))
                if i >= k and nums[i-k] >= large[0][0]:
                    move(small, large)

        def move(h1, h2):
            n, i = heappop(h1)
            heappush(h2, (-n, i))

        def findMedian():
            # since we keep `len(large) >= len(small)`
            if k % 2 == 1:
                return large[0][0]
            else:
                return (large[0][0] - small[0][0]) / 2

        for i in range(k):
            heappush(small, (-nums[i],i))
        # move half to large
        for _ in range(k - k//2):
            # ensure len(large) >= len(small)
            move(small, large)

        res = [findMedian()]
        for i in range(k, len(nums)):
            add(i)
            # non top ones will not impact result, so only remove top ones which out-of-window
            while large and large[0][1] <= i-k:
                heappop(large)
            while small and small[0][1] <= i-k:
                heappop(small)
            res.append(findMedian())

        return res

    def test(self):
        self.assertEqual([1,-1,-1,3,5,6], self.medianSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
