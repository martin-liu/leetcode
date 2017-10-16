# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note: The solution set must not contain duplicate triplets.

# For example, given array S = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

# Basic idea: sort the nums, then for each num, found 2sum.
class Solution(object):
    def threeSum(self, nums):
        counter = {}
        # fill counter with `num -> count`
        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1

        ret = []
        # if 3+ zeros, then add `[0, 0, 0]`
        if 0 in counter and counter[0] > 2:
            ret.append([0, 0, 0])

        uniqNums = counter.keys()
        # positive numbers
        pos = sorted(p for p in uniqNums if p >= 0)
        # negative numbers
        neg = sorted(n for n in uniqNums if n < 0)

        # travel positive nums from right to left
        for p in reversed(pos):
            # travel negative nums from left to right
            for n in neg:
                target = -(p + n)
                if target in counter:
                    # in case target is actually `p` or `n`, e.g. `2 = -(2 + -4)`
                    if (target == p or target == n) and counter[target] > 1:
                        ret.append([n, target, p])
                    elif target < n:
                        ret.append([target, n, p])
                    elif target > p:
                        ret.append([n, p, target])
        return ret

    def threeSum2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        length = len(nums)
        if length < 3:
            return []

        # sort the nums first
        nums.sort()
        # set to record those already checked nums
        ret = []
        for i in range(length):
            # nums already sorted, so that when nums[i] > 0, there's no solution after `nums[i]`
            if nums[i] > 0:
                continue

            # if already checked this num, then skip
            if i > 0 and nums[i] == nums[i - 1]:
                break

            target = 0 - nums[i]
            # find 2 sum of target
            left = i + 1
            right = length - 1
            while left < right:
                s = nums[left] + nums[right]
                if s < target:
                    left += 1
                elif s > target:
                    right -= 1
                else:
                    # s == target
                    solution = [nums[i], nums[left], nums[right]]
                    ret.append(solution)

                    # ignore equal nums
                    while left < right and nums[left + 1] == nums[left]:
                        left += 1
                    while left < right and nums[right - 1] == nums[right]:
                        right -= 1

                    # both go for 1 step
                    left += 1
                    right -= 1
        return ret


# -----------------------------
import unittest

class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(sorted(s.threeSum([-1, 0, 1, 2, -1, -4])), sorted([[-1, -1, 2], [-1, 0, 1]]))
        self.assertEqual(sorted(s.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6])), sorted([[-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2]]))
