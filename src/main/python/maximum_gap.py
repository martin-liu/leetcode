import unittest
from typing import List

class Solution(unittest.TestCase):
    def maximumGap(self, nums: List[int]) -> int:
        """
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Return 0 if the array contains less than 2 elements.

Example 1:

Input: [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either
             (3,6) or (6,9) has the maximum difference 3.
Example 2:

Input: [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.
Note:

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
Try to solve it in linear time/space

---
Basic idea: like bucket sort, but only maintain max & min in each bucket, the max diff is one of bucket max to next bucket min
"""
        if len(nums) < 2:
            return 0
        elif len(nums) == 2:
            return abs(nums[0]-nums[1])

        minVal = maxVal = nums[0]
        for n in nums:
            minVal = min(minVal, n)
            maxVal = max(maxVal, n)

        # if `maxVal-minVal < len(nums)`, then use 1
        bucketSize = (maxVal - minVal) // len(nums) or 1

        bucketMap = {}
        for n in nums:
            i = (n - minVal) // bucketSize
            if i not in bucketMap:
                bucketMap[i] = (n, n)
            else:
                preMax, preMin = bucketMap[i]
                bucketMap[i] = (max(preMax, n), min(preMin, n))

        ret = 0
        pre = None
        for i in range(len(nums)+1):
            if i in bucketMap:
                if pre is not None:
                    _, currMin = bucketMap[i]
                    preMax, _ = bucketMap[pre]
                    ret = max(ret, currMin - preMax)

                pre = i

        return ret


    def testMax(self):
        self.assertEqual(3, self.maximumGap([3,6,9,1]))
        self.assertEqual(0, self.maximumGap([10]))
        self.assertEqual(0, self.maximumGap([1,1,1,1]))
