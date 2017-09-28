# Given a string, find the length of the longest substring without repeating characters.

# Examples:

# Given "abcabcbb", the answer is "abc", which the length is 3.

# Given "bbbbb", the answer is "b", with the length of 1.

# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Basic idea: use an array to store chars, when found duplication, then reset chars to a substring that start from the duplicated char + 1
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == None:
            return 0

        length = len(s)
        maxLen = 0
        chars = []

        for i in range(length):
            # when duplication found
            if s[i] in chars:
                # reset chars from duplication index + 1, as a new substring
                newStart = chars.index(s[i]) + 1
                chars = chars[newStart:]

            chars.append(s[i])
            length = len(chars)
            maxLen = maxLen if maxLen > length else length

        return maxLen


# -----------------------------
import unittest

class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.lengthOfLongestSubstring("abcabcbb"), 3)
        self.assertEqual(s.lengthOfLongestSubstring("bbb"), 1)
        self.assertEqual(s.lengthOfLongestSubstring("pwwkew"), 3)
        self.assertEqual(s.lengthOfLongestSubstring("dvdf"), 3)
