import unittest
from typing import List

class Solution(unittest.TestCase):
    def sortColors(self, nums: List[int]) -> None:
        """
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?

---
Basic idea: 3 pointers (l: 0, curr: iterate, r: 2)
            """
        if not nums:
            return

        length = len(nums)
        l, curr, r = 0, 0, length - 1
        while curr <= r:
            if nums[curr] == 0:
                nums[curr], nums[l] = nums[l], nums[curr]
                l += 1
                # curr come from left, so that any 2 will already swapped to end, do +1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[r] = nums[r], nums[curr]
                r -= 1
                # curr will not +1 because it can be 0 after swap
            else:
                # case 1
                curr += 1

    def testSortColors(self):
        ar = [0,0,0]
        self.sortColors(ar)
        self.assertEqual(ar, [0, 0, 0])

        ar = [2,0,2,1,1,0]
        self.sortColors(ar)
        self.assertEqual(ar, [0, 0, 1, 1, 2, 2])

        ar = [1,2,0]
        self.sortColors(ar)
        self.assertEqual(ar, [0, 1, 2])

        ar = [2,0,1]
        self.sortColors(ar)
        self.assertEqual(ar, [0, 1, 2])

        ar = [1,2,0,0,2,1,1,2,2]
        self.sortColors(ar)
        self.assertEqual(ar, [0,0,1,1,1,2,2,2,2])
