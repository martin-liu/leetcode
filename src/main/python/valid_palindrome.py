import unittest

class Solution(unittest.TestCase):
    def isPalindrome(self, s: str) -> bool:
        """
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""
        l, r = 0, len(s)-1
        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            if s[l].upper() != s[r].upper():
                return False
            else:
                l += 1
                r -= 1
        return True

    def testPalindrome(self):
        self.assertTrue(self.isPalindrome(""))
        self.assertTrue(self.isPalindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(self.isPalindrome("race a car"))
