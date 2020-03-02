import unittest
from typing import List

class Solution(unittest.TestCase):
        def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
            """
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
            """
            if not nums2:
                return nums1

            len2 = len(nums2)
            len1 = len(nums1) - len2

            i1, i2 = len1 - 1, len2 - 1
            for i in range(len(nums1) - 1, -1 , -1):
                if i2 < 0:
                    return
                elif i1 < 0 or nums1[i1] < nums2[i2]:
                    nums1[i] = nums2[i2]
                    i2 -= 1
                else:
                    nums1[i] = nums1[i1]
                    i1 -= 1

        def testMerge(self):
            nums1 = [1,2,3,0,0,0]
            nums2 = [2,5,6]
            self.merge(nums1, 3, nums2, 2)
            self.assertEqual(nums1, [1,2,2,3,5,6])
