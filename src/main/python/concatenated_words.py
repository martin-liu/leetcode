import unittest
from typing import List

class Trie:
    def __init__(self):
        self.children = {}
        self.word = None

    def insert(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = Trie()
            curr = curr.children[c]
        curr.word = word

class Solution(unittest.TestCase):
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        """
Given a list of words (without duplicates), please write a program that returns all concatenated words in the given list of words.
A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

Example:

Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats";
 "dogcatsdog" can be concatenated by "dog", "cats" and "dog";
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
Note:

The number of elements of the given array will not exceed 10,000
The length sum of elements in the given array will not exceed 600,000.
All the input string will only include lower case letters.
The returned elements order does not matter.

-----
Basic Idea: use trie and dfs
"""
        rootTrie = Trie()
        minL = float('inf')
        for w in words:
            rootTrie.insert(w)
            minL = min(minL, len(w))

        res = []
        def dfs(w, i, trie, match):
            if i == len(w):
                if match >= 2:
                    return True
            else:
                if w[i] not in trie.children:
                    return False
                else:
                    curr = trie.children[w[i]]
                    find = False
                    if curr.word:
                        find = dfs(w, i+1, rootTrie, match + 1)
                    elif i == len(w)-1:
                        return False
                    return find or dfs(w, i+1, curr, match)

        for w in words:
            if dfs(w, 0, rootTrie, 0):
                res.append(w)

        return res

    def test(self):
        self.assertEqual(
            self.findAllConcatenatedWordsInADict(
                ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
            ),
            ["catsdogcats","dogcatsdog","ratcatdogcat"]
        )
