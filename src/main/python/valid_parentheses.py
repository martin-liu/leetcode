# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

# Basic idea: use a stack to push and pop characters
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 0:
            return False

        m = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        stack = []
        # travel the string
        for c in s:
            # if starting tag
            if c in m:
                stack.append(c)
            # if not starting tag, then check if match with last item of stack
            elif not stack or m[stack[-1]] != c:
                # if not match with last item (or no item), means invalid
                return False
            else:
                # if match with last item, then pop up
                stack.pop()

        return not stack


# -----------------------------
import unittest

class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertTrue(s.isValid("()"))
        self.assertTrue(s.isValid("([{{()}}])"))
        self.assertFalse(s.isValid("([{()}}])"))
