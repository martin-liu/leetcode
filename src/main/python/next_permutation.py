# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

# The replacement must be in-place, do not allocate extra memory.

# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1

# 所谓一个排列的下一个排列的意思就是 这一个排列与下一个排列之间没有其他的排列。这就要求这一个排列与下一个排列有尽可能长的共同前缀，也即变化限制在尽可能短的后缀上
# 1. from right to left, find first number s[i]<s[i+1]. If not exist, means permutation already greatest，next permutation is the `reverse` of the nums
# 2. in s[i+1:n-1] find a j that s[j]>s[i]>=s[j+1], swap(s[i], s[j])
# 3. sort s[i+1:n-1]
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length <= 1:
            return

        i = length - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i < 0:
            # already greatest permutation, then just reverse to get the smallest permutation
            nums.reverse()
        else:
            j = i + 1

            # find j that s[j] > s[i] >= s[j+1]
            while j < length and nums[j] > nums[i]:
                j += 1
            j -= 1

            # swap j (the least greater one) with i
            tmp = nums[j]
            nums[j] = nums[i]
            nums[i] = tmp

            # sort tail nums
            nums[i+1:] = sorted(nums[i+1:])


# -----------------------------
import unittest

class Test(unittest.TestCase):
    def test(self):
        s = Solution()

        nums = [1, 2, 3]
        s.nextPermutation(nums)
        self.assertEqual(nums, [1, 3, 2])

        nums = [1, 3, 2]
        s.nextPermutation(nums)
        self.assertEqual(nums, [2, 1, 3])

        nums = [3, 2, 1]
        s.nextPermutation(nums)
        self.assertEqual(nums, [1, 2, 3])

        nums = [1, 1, 5]
        s.nextPermutation(nums)
        self.assertEqual(nums, [1, 5, 1])
