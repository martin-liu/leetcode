import unittest
from typing import List

class Solution(unittest.TestCase):
    def singleNumber(self, nums: List[int]) -> int:
        """
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99

---
Basic idea: Use 2 bits to represent 3 states and ensure same logic apply 3 times back to initial state.

Initial state: hl = 00
State change: `00->01->10->00`
Change Logic: f(hl, i)
        f(00, 0) = 00
        f(01, 0) = 00
        f(10, 0) = 00
        f(00, 1) = 01
        f(01, 1) = 10
        f(10, 1) = 00

One working logic is: (no fix logic)
        l' = ~h & (l ^ i)
        h' = ~l' & (h ^ i)

This can also expand to multiple bits case, i.e h, l is 2 number, i is a int
        """
        h, l = 0, 0
        for num in nums:
            l = ~h & (l ^ num)
            h = ~l & (h ^ num)
        return l

    def testSingleNumber(self):
        self.assertEqual(3, self.singleNumber([2,2,3,2]))
        self.assertEqual(99, self.singleNumber([0,1,0,1,0,1,99]))
