import unittest

class Solution(unittest.TestCase):
    def backspaceCompare(self, S: str, T: str) -> bool:
        """
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?

"""
        s, t = len(S)-1, len(T)-1
        sBack, tBack = 0, 0
        while s >= 0 or t >= 0:
            while s >= 0 and (S[s] == '#' or sBack > 0):
                if S[s] == '#':
                    sBack += 1
                else:
                    sBack -= 1
                s -= 1

            while t >= 0 and (T[t] == '#' or tBack > 0):
                if T[t] == '#':
                    tBack += 1
                else:
                    tBack -= 1
                t -= 1

            if s >= 0 and t >= 0:
                if S[s] == T[t]:
                    s -= 1
                    t -= 1
                else:
                    return False
            elif (s >= 0 and S[s] == '#') or (t >= 0 and T[t] == '#'):
                continue
            else:
                break

        return s == t

    def testBackspaceCompare(self):
        self.assertTrue(self.backspaceCompare("ab##", "c#d#"))
        self.assertTrue(self.backspaceCompare("ab#c", "ad#c"))
        self.assertTrue(self.backspaceCompare("a##c", "#a#c"))
        self.assertTrue(self.backspaceCompare("nzp#o#g", "b#nzp#o#g"))
        self.assertFalse(self.backspaceCompare("bba##c", "#a#c"))
        self.assertFalse(self.backspaceCompare("a#c", "b"))
