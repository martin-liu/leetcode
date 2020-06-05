import unittest
from typing import List
from heapq import heappush, heappop

class Solution(unittest.TestCase):
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        """
You have k lists of sorted integers in ascending order. Find the smallest range that includes at least one number from each of the k lists.

We define the range [a,b] is smaller than range [c,d] if b-a < d-c or a < c if b-a == d-c.



Example 1:

Input: [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
Output: [20,24]
Explanation:
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].


Note:

The given list may contain duplicates, so ascending order means >= here.
1 <= k <= 3500
-105 <= value of elements <= 105.

---
Basic Idea: 2 heaps(min & max). keep pop and push minheap (k-way merge), maxheap only need to push (because pop minheap will not impact max value)
        find global min and local max in each round
"""
        if not nums:
            return []

        def less(a, b):
            if not b:
                return True
            da = a[1]-a[0]
            db = b[1]-b[0]
            return da < db or (da == db and a[0] < b[0])

        minHeap, maxHeap = [], []
        for i, ls in enumerate(nums):
            if not ls:
                return []
            heappush(minHeap, (ls[0], i, 0))
            heappush(maxHeap, -ls[0])

        res = None
        while True:
            minV, i, j = heappop(minHeap)
            newRange = [minV, -maxHeap[0]]
            if less(newRange, res):
                res = newRange
            if j < len(nums[i])-1:
                heappush(minHeap, (nums[i][j+1], i, j+1))
                heappush(maxHeap, -nums[i][j+1])
            else:
                return res

        return res

    def test(self):
        self.assertEqual([20,24], self.smallestRange([[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]))
