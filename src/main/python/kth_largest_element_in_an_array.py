import unittest
from typing import List
from heapq import heappush, heappop

class Solution(unittest.TestCase):
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.

"""
        heap = []
        for n in nums:
            if not heap or len(heap) > k or n > heap[0]:
                heappush(heap, n)
                if len(heap) > k:
                    heappop(heap)
        return heap[0]

    def test(self):
        self.assertEqual(5, self.findKthLargest([3,2,1,5,6,4], 2))
        self.assertEqual(4, self.findKthLargest([3,2,3,1,2,4,5,5,6], 4))
