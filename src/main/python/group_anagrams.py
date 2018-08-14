"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""

# Basic idea: sort string, then use a map to collect group
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        m = {}
        for s in strs:
            k = tuple(sorted(s))
            if not k in m:
                m[k] = [s]
            else:
                m[k].append(s)

        return list(m.values())



# -----------------------------
import unittest

class Test(unittest.TestCase):
    def test(self):
        s = Solution()

        self.assertEquals(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]), [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']])
