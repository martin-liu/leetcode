import unittest

class Solution(unittest.TestCase):
    def reverseBits(self, n: int) -> int:
        """
Reverse bits of a given 32 bits unsigned integer.

Example 1:

Input: 00000010100101000001111010011100
Output: 00111001011110000010100101000000
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.

Example 2:

Input: 11111111111111111111111111111101
Output: 10111111111111111111111111111111
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.
"""
        ret = 0
        for _ in range(32):
            bit = n % 2
            n = n >> 1
            ret = (ret << 1) + bit
        return ret

    def testReverseBits(self):
        self.assertEqual(964176192, self.reverseBits(43261596))
        self.assertEqual(3221225471, self.reverseBits(4294967293))
