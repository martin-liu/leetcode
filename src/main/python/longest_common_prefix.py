# Write a function to find the longest common prefix string amongst an array of strings.


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == None or len(strs) == 0:
            return ""

        prefix = strs[0]
        for s in strs:
            while prefix != "" and not s.startswith(prefix):
                prefix = prefix[:-1]
            if prefix == "":
                return ""

        return prefix




# -----------------------------
import unittest

class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.longestCommonPrefix([]), "")
        self.assertEqual(s.longestCommonPrefix(["abc", "acd", "aef"]), "a")
