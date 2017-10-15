# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

#     For example, given array S = {-1 2 1 -4}, and target = 1.

#     The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

# Basic idea: sort the array, from left and right check
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        length = len(nums)
        if length <= 3:
            return sum(nums)
        else:
            # sort the nums first
            nums = sorted(nums)
            minSum = nums[0] + nums[1] + nums[2]
            # if minimum of the sum greater than target
            if minSum >= target:
                return minSum

            maxSum = nums[-3] + nums[-2] + nums[-1]
            if maxSum <= target:
                return maxSum

            if target - minSum < maxSum - target:
                closest = minSum
                distance = target - minSum
            else:
                closest = maxSum
                distance = maxSum - target

            for i in range(length - 2):
                # skip if already checked
                if i > 0 and nums[i - 1] == nums[i]:
                    continue

                left = i + 1
                right = length - 1

                while left < right:
                    s = nums[i] + nums[left] + nums[right]
                    dis = abs(target - s)

                    # if get closer
                    if dis < distance:
                        closest = s
                        distance = dis

                    if s == target:
                        return closest
                    elif s < target:
                        # if max sum of current `left to right` less than target, exit
                        if nums[i] + nums[right] * 2 < target:
                            break
                        left += 1
                    else:
                        # if current min sum greater than target, exit
                        if nums[i] + nums[left] * 2 > target:
                            break
                        right -= 1

            return closest


# -----------------------------
import unittest

class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.threeSumClosest([-1, 2, 1, -4], 1), 2)
        self.assertEqual(s.threeSumClosest([0, 2, 1, -3], 1), 0)
        self.assertEqual(s.threeSumClosest([1,-3,3,5,4,1], 1), 1)
        self.assertEqual(s.threeSumClosest([-1,0,1,1,55], 3), 2)
