import unittest

class Solution(unittest.TestCase):
    def reverseWords(self, s: str) -> str:
        """
Given an input string, reverse the string word by word.

Example 1:

Input: "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.


Note:

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.


Follow up:

For C programmers, try to solve it in-place in O(1) extra space.


"""
        if not s:
            return s

        words = []
        s = " " + s
        curr = ""
        for i in range(len(s)-1, -1, -1):
            if s[i] == ' ':
                if curr != "":
                    words.append(curr)
                curr = ""
            else:
                curr = s[i] + curr

        return " ".join(words)

    def testReverse(self):
        self.assertEqual("blue is sky the", self.reverseWords("the sky is blue"))
        self.assertEqual("world! hello", self.reverseWords("  hello world!  "))
        self.assertEqual("example good a", self.reverseWords("a good   example"))
