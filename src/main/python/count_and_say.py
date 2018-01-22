"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
"""

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        if n < 1:
            return None
        elif n == 1:
            return "1"

        pair = ["1", "11"]

        for i in range(2, n):
            pair[0] = pair[1]

            s = ""
            curr = pair[0][0]
            num = 0

            for c in pair[0]:
                if c == curr:
                    # count same char
                    num += 1
                else:
                    # char changed, then add count and num to string
                    s += str(num) + curr
                    # reset char and num
                    curr = c
                    num = 1

            # last round of the for loop is not added to string
            s += str(num) + curr

            pair[1] = s

        return pair[1]

# -----------------------------
import unittest

class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.countAndSay(1), "1")
        self.assertEqual(s.countAndSay(2), "11")
        self.assertEqual(s.countAndSay(3), "21")
        self.assertEqual(s.countAndSay(4), "1211")
        self.assertEqual(s.countAndSay(5), "111221")
        self.assertEqual(s.countAndSay(6), "312211")
