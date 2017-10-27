# Given an array of integers, find two numbers such that they add up to a specific target number.

# The function twoSum should return indices of the two numbers such that they add
# up to the target, where index1 must be less than index2.
# Please note that your returned answers (both index1 and index2) are not zero-based.

# You may assume that each input would have exactly one solution.

# Input: numbers=[2, 7, 11, 15], target=9
# Output: [0, 1]

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sumMap = {}
        for i in range(len(nums)):
            num = nums[i]
            if (sumMap.get(num) == None):
                # `target - num`
                sumMap[target - num] = i
            else:
                return [sumMap.get(num), i]



# -----------------------------
import unittest

class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        ar = [2, 7, 11, 15]
        self.assertEqual(s.twoSum(ar, 9), [0, 1])
        self.assertEqual(s.twoSum(ar, 13), [0, 2])
        self.assertEqual(s.twoSum(ar, 17), [0, 3])
        self.assertEqual(s.twoSum(ar, 18), [1, 2])
        self.assertEqual(s.twoSum(ar, 22), [1, 3])
        self.assertEqual(s.twoSum(ar, 26), [2, 3])
