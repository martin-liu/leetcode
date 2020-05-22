import unittest
from typing import List

class Solution(unittest.TestCase):
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example:

Input:
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]


Note:

All inputs are consist of lowercase letters a-z.
The values of words are distinct.

---
Basic Idea: Trie with DFS, mark to '#' in one round to prevent cyclic
"""
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

        trie = Trie()
        # build Trie
        for w in words:
            trie.insert(w)

        row, col = len(board), len(board[0])

        res = []
        def dfs(x, y, trie, path):
            if x < 0 or x >= row or y < 0 or y >= col or not trie:
                return
            curr = board[x][y]
            if curr in trie.children:
                trie = trie.children[curr]
                if trie.word and trie.word not in res:
                    res.append(trie.word)

                # mark as '#' so that it will not back to current position
                board[x][y] = '#'
                dfs(x-1, y, trie, path)
                dfs(x+1, y, trie, path)
                dfs(x, y-1, trie, path)
                dfs(x, y+1, trie, path)
                # revert for next round
                board[x][y] = curr

        for i in range(row):
            for j in range(col):
                dfs(i, j, trie, [])

        return res

    def findWords2(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not words:
            return []
        prefixMap, wordMap, minLen, maxLen = {}, {}, float('inf'), -1
        for w in words:
            prefixMap[w[0]] = True
            wordMap[w] = True
            minLen = min(minLen, len(w))
            maxLen = max(maxLen, len(w))

        row, col = len(board), len(board[0])
        res = []

        def getSurround(x, y):
            pos = []
            if x > 0:
                pos.append((x-1,y))
            if x < row-1:
                pos.append((x+1,y))
            if y > 0:
                pos.append((x,y-1))
            if y < col-1:
                pos.append((x,y+1))
            return pos

        def backtrack(track):
            if len(track) > maxLen:
                return
            else:
                if len(track) >= minLen:
                    word = "".join(map(lambda d: board[d[0]][d[1]], track))
                    if word in wordMap and word not in res:
                        res.append(word)

                x, y = track[-1]
                for p in getSurround(x, y):
                    if p not in track:
                        backtrack(track + [p])

        for i in range(row):
            for j in range(col):
                if board[i][j] in prefixMap:
                    backtrack([(i,j)])

        return res

    def test(self):
        self.assertCountEqual([], self.findWords([['a', 'a']], ['aaa']))
        self.assertCountEqual(["eat","oath"], self.findWords(
            [
                ['o','a','a','n'],
                ['e','t','a','e'],
                ['i','h','k','r'],
                ['i','f','l','v']
            ], ["oath","pea","eat","rain"]))
