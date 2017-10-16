# Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

# Note: The solution set must not contain duplicate quadruplets.

# For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]

# Basic idea: create nSum method
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        length = len(nums)
        if length < 4:
            return []

        # sort
        nums = sorted(nums)
        return self.nSum(nums, target, 4)

    # consider nums already sorted
    def nSum(self, nums, target, n):
        ret = []
        if n < 0:
            return ret
        elif n == 1:
            for n in nums:
                if n == target:
                    return [[n]]
        elif n == 2:
            left = 0
            right = len(nums) - 1

            # 2sum
            while left < right:
                cur = nums[left] + nums[right]

                if target < cur:
                    right -= 1
                elif target > cur:
                    left += 1
                else:
                    # found
                    ret.append([nums[left], nums[right]])

                    # both go ahead, because already found the pair, no way to have another pair
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        else:
            # n > 2
            for i in range(len(nums) - n + 1):
                # nums already sorted, so that when nums[i] > target and nums[i] >= 0, there's no solution after `nums[i]`
                if nums[i] > target and nums[i] >= 0:
                    break

                for r in self.nSum(nums[i+1:], target - nums[i], n - 1):
                    solution = [nums[i]] + r
                    if solution not in ret:
                        ret.append(solution)

        return ret



# -----------------------------
import unittest

class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(sorted(s.fourSum([1, 0, -1, 0, -2, 2], 0)), sorted([
            [-1,  0, 0, 1],
            [-2, -1, 1, 2],
            [-2,  0, 0, 2]
        ]))
        self.assertEqual(sorted(s.fourSum([-3,-2,-1,0,0,1,2,3], 0)), sorted([
            [-3,-2,2,3],
            [-3,-1,1,3],
            [-3,0,0,3],
            [-3,0,1,2],
            [-2,-1,0,3],
            [-2,-1,1,2],
            [-2,0,0,2],
            [-1,0,0,1]
        ]))
        self.assertEqual(sorted(s.fourSum([1,-2,-5,-4,-3,3,3,5], -11)), [[-5,-4,-3,1]])
