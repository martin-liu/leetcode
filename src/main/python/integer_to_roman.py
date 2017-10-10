# Given an integer, convert it to a roman numeral.

# Input is guaranteed to be within the range from 1 to 3999.

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        romanMap = {
            1000: 'M',
            500: 'D',
            100: 'C',
            50: 'L',
            10: 'X',
            5: 'V',
            1: 'I'
        }
        prefixUnitMap = {
            1000: 100,
            500: 100,
            100: 10,
            50: 10,
            10: 1,
            5: 1
        }

        ret = ''
        for k in [1000, 500, 100, 50, 10, 5, 1]:
            # get q and r, update num as remainder
            (q, num) = divmod(num, k)

            unit = romanMap[k]
            ret += q * unit

            # do roman subtraction process if need
            if k in prefixUnitMap:
                prefixUnit = romanMap[prefixUnitMap[k]]

                sub = k - prefixUnitMap[k]
                # if meet sub rule
                if num // sub == 1:
                    # append sub style
                    ret += prefixUnit + unit
                    # subtract the sub
                    num -= sub

        return ret



# -----------------------------
import unittest

class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.intToRoman(4), 'IV')
        self.assertEqual(s.intToRoman(1), 'I')
        self.assertEqual(s.intToRoman(2), 'II')
        self.assertEqual(s.intToRoman(8), 'VIII')
        self.assertEqual(s.intToRoman(9), 'IX')
        self.assertEqual(s.intToRoman(40), 'XL')
        self.assertEqual(s.intToRoman(450), 'CDL')
        self.assertEqual(s.intToRoman(1998), 'MCMXCVIII')
