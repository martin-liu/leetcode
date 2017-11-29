# Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# Example:

# Given nums = [1,1,2],

# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
# It doesn't matter what you leave beyond the new length.

# Basic idea: use map to determine duplication
class Solution(object):
    def removeDuplicates2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        curr = 0
        m = {}
        for i in range(len(nums)):
            if nums[i] not in m:
                m[nums[i]] = True
                nums[curr] = nums[i]
                curr += 1

        return curr

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums[:] = set(nums)
        return len(nums)


# -----------------------------
import unittest

class Test(unittest.TestCase):
    def test(self):
        s = Solution()

        self.assertEqual(s.removeDuplicates([1, 1, 2]), 2)
