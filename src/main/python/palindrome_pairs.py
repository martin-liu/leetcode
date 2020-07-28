import unittest
from typing import List

class Trie:
    def __init__(self):
        self.children = {}
        self.index = None

    def insert(self, word, i):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = Trie()
            curr = curr.children[c]
        curr.index = i

    def search(self, prefix):
        curr = self
        indexes = []
        for c in prefix:
            if c not in curr.children:
                # unmatched part can still be pal, so don't return
                break
            if curr.index is not None:
                # unmatched part can still be pal, so count any met word
                indexes.append(curr.index)
            curr = curr.children[c]

        # find all words with matched prefix (part)
        def dfs(trie):
            if trie.index is not None:
                indexes.append(trie.index)
            for c in trie.children.values():
                dfs(c)
        dfs(curr)
        return indexes

class Solution(unittest.TestCase):
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        """
Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:

Input: ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
Example 2:

Input: ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]

------
Basic Idea: Use trie to store reversed words, when search word, match as much as possible.
        The unmatched part can still be pal, so that when meet any word in trie, count it in. And when either no more char in word or trie, don't stop
"""
        trie = Trie()
        empties = []
        for i,w in enumerate(words):
            if not w:
                empties.append(i)
            else:
                # insert reverse of word
                trie.insert(w[::-1], i)

        cache = {}
        def isPal(word):
            if word in cache:
                return cache[word]
            l, r = 0, len(word)-1
            while l < r:
                if word[l] != word[r]:
                    cache[word] = False
                    return False
                l += 1
                r -= 1
            cache[word] = True
            return True

        res = []
        for i,w in enumerate(words):
            # if w is empty, essentially is check any other word is pal
            # if w is not empty, also check empties which essentially check if w is pal
            indexes = list(range(len(words))) if not w else trie.search(w) + empties
            for j in indexes:
                if j != i and isPal(w+words[j]):
                    res.append([i,j])
        return res

    def test(self):
        self.assertCountEqual([[3,0],[1,3],[4,0],[2,4],[5,0],[0,5]], self.palindromePairs(["a","b","c","ab","ac","aa"]))
        self.assertCountEqual([[0,1],[1,0]], self.palindromePairs(["a",""]))
        self.assertCountEqual([[0,1],[1,0],[3,2],[2,4]], self.palindromePairs(["abcd","dcba","lls","s","sssll"]))
        self.assertCountEqual([[0,1],[1,0]], self.palindromePairs(["bat","tab","cat"]))
