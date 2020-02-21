import unittest

class Solution(unittest.TestCase):
    def isNumber(self, s: str) -> bool:
        """
Validate if a given string can be interpreted as a decimal number.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one. However, here is a list of characters that can be in a valid decimal number:

Numbers 0-9
Exponent - "e"
Positive/negative sign - "+"/"-"
Decimal point - "."
Of course, the context of these characters also matters in the input.

---
Basic idea: check if meet `.`, `e` or digit
                """
        if not s:
            return False

        s = s.strip()
        met_dot = met_e = met_digit = False
        for i, char in enumerate(s):
            if char in ['+', '-']:
                # allow +, - after e
                if i > 0 and s[i-1] != 'e':
                    return False
            elif char == '.':
                # no . after e
                if met_dot or met_e:
                    return False
                met_dot = True
            elif char == 'e':
                # e have to after digit
                if met_e or not met_digit:
                    return False
                met_e, met_digit = True, False
            elif char.isdigit():
                met_digit = True
            else:
                return False
        return met_digit

    def testIsNumber(self):
        self.assertFalse(self.isNumber(""))
        self.assertFalse(self.isNumber(" "))
        self.assertFalse(self.isNumber("."))
        self.assertFalse(self.isNumber(".-1"))
        self.assertFalse(self.isNumber(".e1"))
        self.assertFalse(self.isNumber("..2"))
        self.assertFalse(self.isNumber("..2"))
        self.assertFalse(self.isNumber(". 2"))
        self.assertFalse(self.isNumber("e"))
        self.assertFalse(self.isNumber("abc"))
        self.assertFalse(self.isNumber("1 a"))
        self.assertFalse(self.isNumber(" 1e"))
        self.assertFalse(self.isNumber("e3"))
        self.assertFalse(self.isNumber("99e2.5"))
        self.assertFalse(self.isNumber(" --6 "))
        self.assertFalse(self.isNumber("-+3"))
        self.assertFalse(self.isNumber("+0e-"))
        self.assertFalse(self.isNumber("95a54e53"))
        self.assertTrue(self.isNumber("0"))
        self.assertTrue(self.isNumber(".1"))
        self.assertTrue(self.isNumber("1."))
        self.assertTrue(self.isNumber("1.e3"))
        self.assertTrue(self.isNumber("1.e+3"))
        self.assertTrue(self.isNumber("-1."))
        self.assertTrue(self.isNumber(" 0.1 "))
        self.assertTrue(self.isNumber("2e10"))
        self.assertTrue(self.isNumber(" -90e3 "))
        self.assertTrue(self.isNumber(" 6e-1"))
        self.assertTrue(self.isNumber("53.5e93"))
