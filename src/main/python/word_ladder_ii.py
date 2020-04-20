import unittest
from typing import List
from queue import Queue

class Solution(unittest.TestCase):
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        """
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]

Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

Basic idea: BFS (queue); Word can only duplicate in same level. (if in different level, then exists not shortest)
"""
        # word -> visited level
        wordMap = {w:-1 for w in wordList}
        if endWord not in wordMap:
            return []
        queue = Queue()
        queue.put(([beginWord], 1))

        foundLevel = None
        ret = []
        while not queue.empty():
            (curr, level) = queue.get()
            # if already found in a level, then no need to check next levels
            if foundLevel and level > foundLevel:
                return ret

            for i, c in enumerate(curr[-1]):
                for j in range(97, 123):
                    chg = curr[-1][:i] + chr(j) + curr[-1][i+1:]
                    if chg == endWord:
                        foundLevel = level
                        ret.append(curr + [chg])
                    elif chg in wordMap and (wordMap[chg] == -1 or wordMap[chg] == level):
                        # only allow when not visited or in same level
                        queue.put((curr + [chg], level+1))
                        wordMap[chg] = level

        return ret

    def testLadder(self):
        self.assertEqual([["hit","hot","dot","dog","cog"], ["hit","hot","lot","log","cog"]], self.findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
        self.assertEqual([], self.findLadders("hit", "cog", ["hot","dot","dog","lot","log"]))
        self.assertEqual([["red","ted","tad","tax"],["red","ted","tex","tax"],["red","rex","tex","tax"]], self.findLadders("red", "tax", ["ted","tex","red","tax","tad","den","rex","pee"]))
