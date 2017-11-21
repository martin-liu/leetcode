# Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

# Your algorithm's runtime complexity must be in the order of O(log n).

# If the target is not found in the array, return [-1, -1].

# For example,
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return [3, 4].


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        if len(nums) == 0:
            return [-1, -1]

        length = len(nums)
        start, end = 0, length - 1

        ret = [-1, -1]
        while start <= end:
            mid = (start + end) // 2
            if target == nums[mid]:
                start = mid
                end = mid
                while start >= 0 and nums[start] == nums[mid]:
                    start -= 1
                while end <= length - 1 and nums[end] == nums[mid]:
                    end += 1
                return [start + 1, end - 1]

            elif target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1

        return ret


# -----------------------------
import unittest

class Test(unittest.TestCase):
    def test(self):
        s = Solution()

        self.assertEqual(s.searchRange([5, 7, 7, 8, 8, 10], 8), [3, 4])
        self.assertEqual(s.searchRange([2, 2], 2), [0, 1])
        self.assertEqual(s.searchRange([1], 1), [0, 0])
