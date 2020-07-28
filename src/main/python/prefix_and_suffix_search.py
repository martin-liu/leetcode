import unittest
from typing import List

class Trie:
    def __init__(self):
        self.children = {}
        self.weights = []

    def insert(self, word, weight):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = Trie()
            curr = curr.children[c]
            curr.weights.append(weight)

    def searchWeights(self, prefix):
        curr = self
        for c in prefix:
            if c not in curr.children:
                return []
            curr = curr.children[c]
        return curr.weights

class WordFilter:
    """
Given many words, words[i] has weight i.

Design a class WordFilter that supports one function, WordFilter.f(String prefix, String suffix). It will return the word with given prefix and suffix with maximum weight. If no word exists, return -1.

Examples:

Input:
WordFilter(["apple"])
WordFilter.f("a", "e") // returns 0
WordFilter.f("b", "") // returns -1


Note:

words has length in range [1, 15000].
For each test case, up to words.length queries WordFilter.f may be made.
words[i] has length in range [1, 10].
prefix, suffix have lengths in range [0, 10].
words[i] and prefix, suffix queries consist of lowercase letters only.

----
Basic Idea: use 2 prefix tries, one store word, another store word.reverse(). Each trie node store all weights visited current node.
    When search, search prefix and suffix.reverse() for both tires, then do a max(intersection) to get max weight
"""
    def __init__(self, words: List[str]):
        self.ptrie = Trie()
        self.strie = Trie()
        self.weights = []
        # when duplicate, only last one need to care
        dedupWord = {w:i for i,w in enumerate(words)}
        for w, i in dedupWord.items():
            self.ptrie.insert(w, i)
            self.strie.insert(w[::-1], i)
            self.weights.append(i)

    def f(self, prefix: str, suffix: str) -> int:
        # if no prefix/suffix, treat it match all the weights
        pw = self.weights if not prefix else self.ptrie.searchWeights(prefix)
        sw = self.weights if not suffix else self.strie.searchWeights(suffix[::-1])
        weights = set(pw) & set(sw) or [-1]
        return max(weights)

class Test(unittest.TestCase):
    def test(self):
        wf = WordFilter(["apple"])
        self.assertEqual(0, wf.f("a", "e"))
        self.assertEqual(0, wf.f("", ""))
        self.assertEqual(0, wf.f("a", ""))
        self.assertEqual(0, wf.f("", "e"))
        self.assertEqual(0, wf.f("", "le"))
        self.assertEqual(-1, wf.f("b", ""))

        wf = WordFilter(["abbbababbb","baaabbabbb","abababbaaa","abbbbbbbba","bbbaabbbaa","ababbaabaa","baaaaabbbb","babbabbabb","ababaababb","bbabbababa"])
        self.assertEqual(5, wf.f("", "abaa"))
