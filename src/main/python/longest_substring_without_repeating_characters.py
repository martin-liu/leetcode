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
        if not s:
            return 0

        maxLen = 0
        chars = []

        for i in range(len(s)):
            # when duplication found
            if s[i] in chars:
                # reset chars from duplication index + 1, as a new substring
                newStart = chars.index(s[i]) + 1
                chars = chars[newStart:]

            chars.append(s[i])
            length = len(chars)
            maxLen = max(maxLen, length)

        return maxLen

    def lengthOfLongestSubstring2(seft, s):
        """use map to store char -> index, if a char already in map, means there's a duplication"""
        amap = {}
        left = -1
        maxLen = 0
        for i, v in enumerate(s):
            if v in amap:
                # means find a duplication
                # left should be at the duplicated place
                left = amap[v]

            amap[v] = i
            maxLen = max(maxLen, i - left)
        return maxLen

# -----------------------------
import unittest

class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.lengthOfLongestSubstring(None), 0)
        self.assertEqual(s.lengthOfLongestSubstring(""), 0)
        self.assertEqual(s.lengthOfLongestSubstring("abcabcbb"), 3)
        self.assertEqual(s.lengthOfLongestSubstring2("abcabcbb"), 3)
        self.assertEqual(s.lengthOfLongestSubstring("bbb"), 1)
        self.assertEqual(s.lengthOfLongestSubstring2("bbb"), 1)
        self.assertEqual(s.lengthOfLongestSubstring("pwwkew"), 3)
        self.assertEqual(s.lengthOfLongestSubstring2("pwwkew"), 3)
        self.assertEqual(s.lengthOfLongestSubstring("dvdf"), 3)
        self.assertEqual(s.lengthOfLongestSubstring2("dvdf"), 3)
