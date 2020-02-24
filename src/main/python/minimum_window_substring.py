import unittest

        """
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

---
Basic idea: use an array to store each index of matched char, use a map to store number of a char and indexes in array; when same char match again, set array[i] = -1 to evict first occurence
        """
        if not s or not t:
            return ""

        sLen = len(s)
        tLen = len(t)
        if sLen < tLen:
            return ""

        tmap = {}
        for c in t:
            if c in tmap:
                number, _ = tmap[c]
                tmap[c] = (number + 1, [])
            else:
                tmap[c] = (1, [])

        matches = []
        matchStart = 0
        charsFound = 0

        start, end = -1, -1
        length = None
        for i, c in enumerate(s):
            if c in tmap:
                # char number and indexes in matches array
                number, indexes = tmap[c]
                matches.append(i)
                indexes.append(len(matches) - 1)
                if len(indexes) > number:
                    # more same char matched, mark first occurence as -1
                    matches[indexes.pop(0)] = -1
                    # find new start position
                    while matches[matchStart] == -1:
                        matchStart += 1
                else:
                    # when no char will be evicted
                    charsFound += 1

                # all chars in T is found
                if charsFound == tLen:
                    currLen = matches[-1] - matches[matchStart] + 1
                    if not length or currLen < length:
                        start, end = matches[matchStart], matches[-1]
                        length = currLen
        return s[start:end+1]

    def testMinWindow(self):
        self.assertEqual(self.minWindow("", "ABC"), "")
        self.assertEqual(self.minWindow("ABC", ""), "")
        self.assertEqual(self.minWindow("aa", "aa"), "aa")
        self.assertEqual(self.minWindow("a", "b"), "")
        self.assertEqual(self.minWindow("bba", "ab"), "ba")
        self.assertEqual(self.minWindow("acbbaca", "aba"), "baca")
        self.assertEqual(self.minWindow("ADOBECODEBANC", "ABC"), "BANC")
