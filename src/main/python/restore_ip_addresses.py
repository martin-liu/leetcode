import unittest
from typing import List

class Solution(unittest.TestCase):
    def restoreIpAddresses(self, s: str) -> List[str]:
        """
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
        """
        if not s or len(s) < 4 or len(s) > 12:
            return []

        length = len(s)
        ret = []
        selections = [1, 2, 3]
        def backtrack(track):
            if len(track) == 4:
                i, ip = 0, ""
                for n in track:
                   ip += s[i:i+n] + '.'
                   i += n
                ret.append(ip[:-1])
                return

            for n in selections:
                trackSum = sum(track)
                # if length cannot meet
                if (3-len(track)) * 3 + trackSum + n < length or trackSum >= length:
                    continue
                # if total length not match
                if len(track) == 3 and trackSum + n != length:
                    continue
                # if `0..`
                if n > 1 and s[trackSum] == '0':
                    continue
                num = int(s[trackSum:trackSum+n] or '0')
                if num > 255:
                    continue
                backtrack(track + [n])

        backtrack([])

        return ret

    def testRestoreIpAddresses(self):
        self.assertEqual(self.restoreIpAddresses(""), [])
        self.assertEqual(self.restoreIpAddresses("25525511135"), ["255.255.11.135", "255.255.111.35"])
