# You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

# For example, given:
# s: "barfoothefoobarman"
# words: ["foo", "bar"]

# You should return the indices: [0,9].
# (order does not matter).

# Basic idea: check at most wordLength rounds, every round jump to check all words
# e.g. s: "barfoothefoobarman", words: ["foo", "bar"]
# starts with (`bar`, `arf`, `rfo`), jump 3 chars to check

class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        if len(s) == 0 or len(words) == 0:
            return []

        ret = []
        strLength = len(s)
        wordLength = len(words[0])
        subStrLength = len(words) * wordLength

        if subStrLength > strLength:
            return []

        # setup times of word in map
        times = {}
        for x in words:
            times[x] = (times.get(x) or 0) + 1

        # not check every char, because we will jump by wordLength
        for start in range(min(wordLength, strLength - subStrLength + 1)):
            match = True
            subStr = s[start:(start + subStrLength)]

            curr = {}
            end = start
            while start + subStrLength <= strLength:
                word = s[end:(end + wordLength)]
                end += wordLength

                if word not in times:
                    # skip this word and restart check (jump to next work)
                    start = end
                    curr.clear()
                else:
                    if word in curr:
                        curr[word] += 1
                    else:
                        curr[word] = 1

                    while curr[word] > times[word]:
                        # if word occurs more then specified times (invalid), then try skip first word until it valid
                        curr[s[start:(start + wordLength)]] -= 1
                        start += wordLength

                    # when stable, if start to end is exactly the length we want, means match
                    if end - start == subStrLength:
                        ret.append(start)

        return ret

# -----------------------------
import unittest

class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.findSubstring("", ["foo", "bar"]), [])
        self.assertEqual(s.findSubstring("barfoothefoobarman", ["foo", "bar"]), [0, 9])
        self.assertEqual(s.findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]), [6, 9, 12])
        self.assertEqual(s.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"]), [8])
        self.assertEqual(s.findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo","barr","wing","ding","wing"]), [13])
