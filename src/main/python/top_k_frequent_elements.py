import unittest
from typing import List
from collections import Counter
from heapq import heappush, heappop

class Solution(unittest.TestCase):
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
You can return the answer in any order.

Basic Idea: times <= len(nums), so just build map<count, num>, then iterate len(nums)..0
"""
        d = {}
        for n, c in Counter(nums).items():
            d[c] = d.get(c, []) + [n]

        res = []
        for i in range(len(nums), -1, -1):
            for n in d.get(i, []):
                if len(res) < k:
                    res.append(n)
                else:
                    return res
        return res

    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        d = dict()
        for n in nums:
            d[n] = d.get(n, 0) + 1

        heap, store = [], {}
        for n, t in d.items():
            store[t] = store.get(t, []) + [n]
            if not heap or len(heap) < k or t > heap[0]:
                heappush(heap, t)
                if len(heap) > k:
                    heappop(heap)

        res = []
        for t in heap:
            for n in store[t]:
                if len(res) < k:
                    if n not in res:
                        res.append(n)
                else:
                    return res
        return res

    def test(self):
        self.assertCountEqual([1,2], self.topKFrequent([1,1,1,2,2,3], 2))
        self.assertCountEqual([1,2], self.topKFrequent([1,1,2,2,3], 2))
        self.assertCountEqual([1], self.topKFrequent([1], 1))
        self.assertCountEqual([1,3,5], self.topKFrequent([5,3,1,1,1,3,5,73,1], 3))
