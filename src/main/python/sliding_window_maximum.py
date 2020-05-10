import unittest
from typing import List

from collections import deque
class Solution(unittest.TestCase):
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Follow up:
Could you solve it in linear time?

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7]
Explanation:

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7


Constraints:

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= nums.length

        """
        if not nums:
            return None
        length = len(nums)
        if length <= k:
            return [max(nums)]
        ret = []
        # deque is a structure that can be both queue or stack, typically is implemented via circular array or  linked list
        # use deque to store index of maximums of each window slide
        dq = deque()
        for i, n in enumerate(nums):
            # remove every element that smaller, so that keep the deque in order from max to second max, etc.
            while dq and nums[dq[-1]] < n:
                dq.pop()
            dq.append(i)
            # if left el is not in current window, then remove it
            if i - dq[0] > k - 1:
                dq.popleft()
            if i >= k - 1:
                ret.append(nums[dq[0]])
        return ret

    def testSliding(self):
        self.assertEqual([3,3,5,5,6,7], self.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
