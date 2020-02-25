import unittest
from typing import List

class Solution(unittest.TestCase):
    def removeDuplicates(self, nums: List[int]) -> int:
        """
Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,1,2,3,3],

Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.

It doesn't matter what values are set beyond the returned length.
Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
(nums[i]);

}

---
Basic idea: iterate nums, count max 2 times for a number, then use a counter `shift=skippedNum` to decide the gap to shift, `nums[i-shift]=nums[i]`
        """
        if not nums:
            return 0

        curr, count, shift = nums[0], 0, 0
        ret = 0
        for i, n in enumerate(nums):
            if n == curr:
                count += 1
                if count > 2:
                    # when greater than 2, don't count it, add to shift
                    shift += 1
                    continue
            else:
                curr = n
                count = 1
            ret += 1

            # do shift after normal counting
            if shift > 0:
                nums[i-shift] = nums[i]

        return ret

    def testRemoveDuplicates(self):
        self.assertEqual(self.removeDuplicates([1,1,1,2,2,3]), 5)
        self.assertEqual(self.removeDuplicates([0,0,1,1,1,1,2,3,3]), 7)
