# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You may assume no duplicates in the array.

# Example 1:
# Input: [1,3,5,6], 5
# Output: 2

# Example 2:
# Input: [1,3,5,6], 2
# Output: 1

# Example 3:
# Input: [1,3,5,6], 7
# Output: 4

# Example 4:
# Input: [1,3,5,6], 0
# Output: 0

# Basic idea: binary search, but when move left, do `end = mid` rather `end = mid - 1`, so that end always greater than target
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        start, end = 0, length

        while start < end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                # only reduce to `mid` rather than `mid - 1`, so that `end` always greater than target
                # hence when process finished, start/end will stop at the correct index which greater than target
                end = mid
            else:
                start = mid + 1

        # now `start` equals `end`, return any of them
        return start

# -----------------------------
import unittest

class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.searchInsert([1, 3, 5, 6], 5), 2)
        self.assertEqual(s.searchInsert([1, 3, 5, 6], 2), 1)
        self.assertEqual(s.searchInsert([1, 3, 5, 6], 7), 4)
        self.assertEqual(s.searchInsert([1, 3, 5, 6], 0), 0)
