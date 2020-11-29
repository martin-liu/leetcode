# There are two sorted arrays nums1 and nums2 of size m and n respectively.

# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

# Example 1:
# nums1 = [1, 3]
# nums2 = [2]

# The median is 2.0

# Example 2:
# nums1 = [1, 2]
# nums2 = [3, 4]

# The median is (2 + 3)/2 = 2.5


# Basic idea: Create an union array and then calculate the median
from heapq import heappush, heappop
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        2 heaps, one min heap store greater values, one max heap store smaller values
        keep length diff <= 1
        """
        if not nums1 and not nums2:
            return 0
        l1, l2, minH, maxH = len(nums1), len(nums2), [], []
        isOdd = (l1 + l2) & 1 == 1

        for n in nums1 + nums2:
            if not minH or n > minH[0]:
                heappush(minH, n)
            else:
                heappush(maxH, -n)

            if len(minH) - len(maxH) > 1:
                heappush(maxH, - heappop(minH))
            elif len(maxH) - len(minH) > 1:
                heappush(minH, - heappop(maxH))

        if isOdd:
            return minH[0] if len(minH) > len(maxH) else -maxH[0]
        else:
            return (minH[0] - maxH[0]) / 2

    def findMedianSortedArrays2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if not nums1 and not nums2:
            return 0

        len1 = len(nums1)
        len2 = len(nums2)
        lenTotal = len1 + len2
        i1 = 0
        i2 = 0

        even = lenTotal % 2 == 0
        mid = lenTotal // 2
        union = []

        # union no need to be full union, only need 0 ~ mid
        while i1 + i2 < mid + 1:
            # if i1 reach len1, then only add nums2's element to union
            if i1 == len1:
                union.append(nums2[i2])
                i2 += 1
            # if i2 reach len2, then only add nums1's element to union
            elif i2 == len2:
                union.append(nums1[i1])
                i1 += 1
            # if nums1[i1] is smaller, then add it to union
            elif nums1[i1] <= nums2[i2]:
                union.append(nums1[i1])
                i1 += 1
            # if nums2[i2] is smaller, then add it to union
            else:
                union.append(nums2[i2])
                i2 += 1

        if even:
            return float(union[mid] + union[mid - 1]) / 2
        else:
            return float(union[mid])



# -----------------------------
import unittest

class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.findMedianSortedArrays([], [2]), 2.0)
        self.assertEqual(s.findMedianSortedArrays([], []), 0)
        self.assertEqual(s.findMedianSortedArrays([1], [2]), 1.5)
        self.assertEqual(s.findMedianSortedArrays([1, 3], [2]), 2.0)
        self.assertEqual(s.findMedianSortedArrays([1, 2], [3, 4]), 2.5)
