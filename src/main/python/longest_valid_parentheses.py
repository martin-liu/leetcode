# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

# For "(()", the longest valid parentheses substring is "()", which has length = 2.

# Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.

# Basic idea: store index of `(` in stack, so that when pop, we can use index deduction to get length
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        stack = []
        last = 0
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif not stack:
                # c is `)`, stack is empty. Then skip it
                last = i + 1
            else:
                # c is `)`, stack is not empty, means it match from last index to current index
                # then pop
                stack.pop()
                if not stack:
                    # if stack is empty, last index is `last`
                    ret = max(ret, i - last + 1)
                else:
                    # if stack is not empty, last index is `stack[-1]`
                    ret = max(ret, i - stack[-1])

        return ret

# -----------------------------
import unittest

class Test(unittest.TestCase):
    def test(self):
        s = Solution()

        self.assertEqual(s.longestValidParentheses(""), 0)
        self.assertEqual(s.longestValidParentheses("(()"), 2)
        self.assertEqual(s.longestValidParentheses(")()())"), 4)
        self.assertEqual(s.longestValidParentheses("()(()"), 2)
        self.assertEqual(s.longestValidParentheses("(()(((()"), 2)
        self.assertEqual(s.longestValidParentheses(")()())()()("), 4)
        self.assertEqual(s.longestValidParentheses("(()))())("), 4)
        self.assertEqual(s.longestValidParentheses(")(())))(())())"), 6)
