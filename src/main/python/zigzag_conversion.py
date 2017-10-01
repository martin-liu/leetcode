# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R

# 2 rows example:
# A C E
# B D

# 4 rows example:
# A   G   M
# B F H L N
# C E I K O
# D   J

# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string text, int nRows);
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

# Basic idea: fill 2 dimension array, if numRows > 2, then skip `oddCol & (first or last row)`; when oddCol, reverse fill order in that col
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if s == None or len(s) <= numRows:
            return s
        else:
            ar = []
            for i in range(numRows):
                ar.append([])

            # current cursor index of `s`
            sIndex = 0
            # current global travel index
            travel = 0
            while sIndex < len(s):
                col = travel // numRows
                row = travel % numRows
                isOddCol = col % 2 == 1

                if numRows <= 2:
                    # if numRows less or equal than 2, then don't skip any element
                    isSkip = False
                else:
                    # if numRows > 2, then skip first and last row in odd col
                    isSkip = (row == 0 or row == numRows - 1) and isOddCol

                    if isOddCol:
                        # if odd col, then reverse the order
                        row = numRows - 1 - row

                if not isSkip:
                  ar[row].append(s[sIndex])
                  sIndex += 1

                travel += 1

            return "".join(map("".join, ar))


# -----------------------------
import unittest

class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.convert("ABC", 2), "ACB")
        self.assertEqual(s.convert("ABCDE", 4), "ABCED")
        self.assertEqual(s.convert("ABCDEF", 4), "ABFCED")
        self.assertEqual(s.convert("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR")
