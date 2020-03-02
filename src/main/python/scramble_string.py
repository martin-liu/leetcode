import unittest

class Solution(unittest.TestCase):
    def isScramble(self, s1: str, s2: str) -> bool:
        """
Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.

Example 1:

Input: s1 = "great", s2 = "rgeat"
Output: true
Example 2:

Input: s1 = "abcde", s2 = "caebd"
Output: false

---
Basic idea: ensure chars are same via sorted(s1) == sorted(s2), then recursively check if left/right == left/right or left/right == right/left
        """

        if not s1 or not s2 or len(s1) != len(s2):
            return False
        length = len(s1)

        if s1 == s2:
            return True
        elif sorted(s1) != sorted(s2):
            # if chars are different
            return False
        else:
            for i in range(length-1):
                # left/right == left/right
                if self.isScramble(s1[:i+1], s2[:i+1]) and self.isScramble(s1[i+1:], s2[i+1:]):
                    return True
                # left/right == right/left
                if self.isScramble(s1[:i+1], s2[length-i-1:]) and self.isScramble(s1[i+1:], s2[:length-i-1]):
                    return True

        return False

    def testIsScramble(self):
        self.assertTrue(self.isScramble("great", "rgeat"))
        self.assertTrue(self.isScramble("great", "rgtae"))
        self.assertFalse(self.isScramble("abcde", "caebd"))
        self.assertFalse(self.isScramble("abcdefghijklmnopq","efghijklmnopqcadb"))
