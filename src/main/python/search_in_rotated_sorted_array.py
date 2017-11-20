# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

# You are given a target value to search. If found in the array return its index, otherwise return -1.

# You may assume no duplicate exists in the array.

# Basic idea: use binary search, but only check non rotated part, leave rotated part to next round
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1

        start, end = 0, len(nums) - 1

        while start < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                # match
                return mid
            elif nums[start] <= nums[mid]:
                # start <= mid, means no rotation bewteen [start, mid]
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                # start > mid, means no rotation bewteen [mid, end]
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1

        if nums[start] == target:
            return start


        return -1

# -----------------------------
import unittest

class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.search([0, 1, 2, 3, 4, 5, 6, 7], 3), 3)
        self.assertEqual(s.search([0, 1, 2, 3, 4, 5, 6, 7], 5), 5)
        self.assertEqual(s.search([3, 4, 5, 6, 7, 0, 1, 2], 3), 0)
        self.assertEqual(s.search([4, 5, 6, 7, 0, 1, 2, 3], 1), 5)
        self.assertEqual(s.search([4, 5, 6, 7, 0, 1, 2, 3], 7), 3)
        self.assertEqual(s.search([4, 5, 6, 7, 0, 1, 2, 3], 0), 4)
        self.assertEqual(s.search([4, 5, 6, 7, 8, 9, 0, 1, 2, 3], 9), 5)
        self.assertEqual(s.search([5,1,2,3,4], 1), 1)
