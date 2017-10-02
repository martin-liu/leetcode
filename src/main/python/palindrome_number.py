# Determine whether an integer is a palindrome. Do this without extra space.

# Some hints:
# Could negative integers be palindromes? (ie, -1)

# If you are thinking of converting the integer to string, note the restriction of using extra space.

# You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

# There is a more generic way of solving this problem.


# Basic idea: reverse the integer, see if it's same as original
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x == None or x < 0:
            return False

        if x < 10:
            return True

        INT_MAX = 2 ** 31 + 1
        t = x
        p = 0
        while t > 0:
            (t, r) = divmod(t, 10)

            # check overflow
            if (INT_MAX - r) / 10 < p:
                return False

            p = p * 10 + r

        return p == x

# -----------------------------
import unittest

class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertTrue(s.isPalindrome(1))
        self.assertTrue(s.isPalindrome(121))
        self.assertFalse(s.isPalindrome(None))
        self.assertFalse(s.isPalindrome(-121))
        self.assertFalse(s.isPalindrome(12))
