import unittest
from typing import List

class Solution(unittest.TestCase):
    def rotate(self, nums: List[int], k: int) -> None:
        """
Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?


Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]


Constraints:

1 <= nums.length <= 2 * 10^4
It's guaranteed that nums[i] fits in a 32 bit-signed integer.
k >= 0

---
Basic Idea: there'll be `gcd(n,k)` number of circles in the array, swap in each circle
        e.g. [1,2,3,4], k = 2;
        gcd = 2
        2 circles: 1 -> 3 -> 1, 2 -> 4 -> 2
        """
        k = k % len(nums)
        if k == 0:
            return nums

        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)

        GCD = gcd(len(nums), k)
        # based on GCD, swap all the circles
        for i in range(GCD):
            j = (i + k) % len(nums)
            tmp = nums[i]
            # swap in a circle
            while j != i:
                nums[j], tmp = tmp, nums[j]
                j = (j + k) % len(nums)
            nums[i] = tmp

    def testRotate(self):
        nums = [1,2,3,4,5,6,7]
        self.rotate(nums, 1)
        self.assertEqual([7,1,2,3,4,5,6], nums)
        self.rotate(nums, 2)
        self.assertEqual([5,6,7,1,2,3,4], nums)

        nums = [-1,-100,3,99]
        self.rotate(nums, 2)
        self.assertEqual([3,99,-1,-100], nums)
