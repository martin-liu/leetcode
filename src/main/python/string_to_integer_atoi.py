# Implement atoi to convert a string to an integer.

# Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

# Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

# Requirements for atoi:
# The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

# The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

# If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

# If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.

# Basic idea: char -> int map
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MAX = 2147483647
        INT_MIN = -2147483648

        length = len(str)

        # ignore whitespace
        n = 0
        while n < length and str[n] == " ":
            n += 1

        if n == length:
            # all chars are whitespace or str is empty
            return 0

        # kill prefix whitespace
        str = str[n:]
        minus = False
        if str[0] == '-' or str[0] == '+':
            if str[0] == '-':
                minus = True

            str = str[1:]

        ret = 0
        for i in range(len(str)):
            n = self.charToInt(str[i])
            # if any char rather than number found, then return current value
            if n == None:
                return ret

            if minus == True:
                # check overflow
                if (INT_MIN + n) / 10 >= ret:
                    return INT_MIN
                ret = ret * 10 - n
            else:
                # check overflow
                if (INT_MAX - n) / 10 <= ret:
                    return INT_MAX
                ret = ret * 10 + n

        return ret

    def charToInt(self, c):
        m = {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9
        }
        return m.get(c)


# -----------------------------
import unittest

class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.myAtoi(""), 0)
        self.assertEqual(s.myAtoi("+-2"), 0)
        self.assertEqual(s.myAtoi("-325"), -325)
        self.assertEqual(s.myAtoi("+125"), 125)
        self.assertEqual(s.myAtoi("  +125 "), 125)
        self.assertEqual(s.myAtoi("-2147483649"), -2147483648)
        self.assertEqual(s.myAtoi("2147483648"), 2147483647)
        self.assertEqual(s.myAtoi("    10522545459"), 2147483647)
        self.assertEqual(s.myAtoi("-2147483648"), -2147483648)
