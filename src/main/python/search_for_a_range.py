# Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

# Your algorithm's runtime complexity must be in the order of O(log n).

# If the target is not found in the array, return [-1, -1].

# For example,
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return [3, 4].

# Basic idea: binary search, need to consider that there maybe very huge number of target value
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ret = [-1, -1]
        if not nums:
            return ret

        start, end = 0, len(nums) - 1

        # find start of the target
        while start < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid

        if nums[start] != target:
            return ret

        ret[0] = start
        end = len(nums) - 1

        # find end of the target
        while start < end:
            mid = (start + end + 1) // 2
            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid
        ret[1] = end

        return ret


# -----------------------------
import unittest

class Test(unittest.TestCase):
    def test(self):
        s = Solution()

        self.assertEqual(s.searchRange([5, 7, 7, 8, 8, 10], 8), [3, 4])
        self.assertEqual(s.searchRange([2, 2], 2), [0, 1])
        self.assertEqual(s.searchRange([1], 1), [0, 0])
