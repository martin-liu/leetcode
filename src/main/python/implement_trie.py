import unittest

class Trie:
    """
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
"""

    def __init__(self):
        self.children = [None] * 26
        self.dataPoint = False

    def insert(self, word: str) -> None:
        def ifNone(curr, i):
            curr.children[i] = Trie()
        trie = self._travel(word, ifNone)
        trie.dataPoint = True

    def search(self, word: str) -> bool:
        trie = self._travel(word)
        return trie and trie.dataPoint

    def startsWith(self, prefix: str) -> bool:
        return self._travel(prefix) is not None

    def _travel(self, word, ifNoneFunc=None):
        curr = self
        for c in word:
            i = ord(c)-97
            if not curr.children[i]:
                if ifNoneFunc:
                    ifNoneFunc(curr, i)
                else:
                    return None
            curr = curr.children[i]
        return curr

class Tests(unittest.TestCase):
    def test(self):
        trie = Trie()
        trie.insert("apple")
        self.assertTrue(trie.search("apple"))
        self.assertFalse(trie.search("app"))
        self.assertTrue(trie.startsWith("app"))
        trie.insert("app")
        self.assertTrue(trie.search("app"))
