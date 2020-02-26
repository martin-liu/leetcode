import unittest
from typing import List

class Solution(unittest.TestCase):
    def plusOne(self, digits: List[int]) -> List[int]:
        """
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
        """

        if not digits:
            return []
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            carry, digits[i] = divmod(digits[i]+carry, 10)
            if carry == 0:
                break

        if carry == 1:
            return [1] + digits
        else:
            return digits

    def testPlusOne(self):
        self.assertEqual(self.plusOne([]), [])
        self.assertEqual(self.plusOne([9]), [1,0])
        self.assertEqual(self.plusOne([9,9]), [1,0,0])
        self.assertEqual(self.plusOne([1,2,3]), [1,2,4])
        self.assertEqual(self.plusOne([1,2,9]), [1,3,0])
        self.assertEqual(self.plusOne([1,2,3]), [1,2,4])
        self.assertEqual(self.plusOne([1,2,3]), [1,2,4])
        self.assertEqual(self.plusOne([1,2,3]), [1,2,4])
