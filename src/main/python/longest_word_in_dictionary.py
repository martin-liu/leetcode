import unittest
from typing import List

class Trie(object):
    def __init__(self, isWord=False):
        self.children = [None] * 26
        self.isWord = isWord

class Solution(unittest.TestCase):
    def longestWord(self, words: List[str]) -> str:
        """
Given a list of strings words representing an English Dictionary, find the longest word in words that can be built one character at a time by other words in words. If there is more than one possible answer, return the longest word with the smallest lexicographical order.

If there is no answer, return the empty string.
Example 1:

Input:
words = ["w","wo","wor","worl", "world"]
Output: "world"
Explanation:
The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
Example 2:

Input:
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
Output: "apple"
Explanation:
Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
Note:

All the strings in the input will only contain lowercase letters.
The length of words will be in the range [1, 1000].
The length of words[i] will be in the range [1, 30].
"""
        words.sort(key=lambda w: len(w))
        res, d = "", {}

        def longer(a, b):
            return a < b if len(a) == len(b) else len(a) > len(b)

        for word in words:
            if len(word) == 1:
                d[word] = True
            else:
                valid = True
                for i in range(len(word)-1):
                    if word[:i+1] not in d:
                        valid = False

                if valid:
                    d[word] = True
            if word in d and longer(word, res):
                res = word

        return res

    def longestWord2(self, words: List[str]) -> str:
        if not words:
            return ""
        # sort by length
        words.sort(key=lambda w: len(w))
        if len(words[0]) > 1:
            return ""

        res = ""
        root = Trie()
        preLen, currLen = None, None

        def longer(a, b):
            return a < b if len(a) == len(b) else len(a) > len(b)

        for word in words:
            preLen, currLen = currLen, len(word)
            if preLen is not None and currLen is not None and currLen-preLen > 1:
                break
            curr = root
            for i, c in enumerate(word):
                index = ord(c)-97
                if len(word)-1 == i:
                    curr.children[index] = Trie(True)
                    if longer(word, res):
                        res = word
                elif not curr.children[index] or not curr.children[index].isWord:
                    break
                else:
                    curr = curr.children[index]

        return res

    def test(self):
        self.assertEqual("world", self.longestWord(["w","wo","wor","worl", "world"]))
        self.assertEqual("apple", self.longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"]))
