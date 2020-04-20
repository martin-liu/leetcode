import unittest
from typing import List
from queue import Queue

class Solution(unittest.TestCase):
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

Basic Idea: BFS, change word then check in map; remove visited from map to prevent cyclic
"""
        wordMap = {w:True for w in wordList}
        if endWord not in wordMap:
            return 0
        queue = Queue()
        queue.put((beginWord, 1))

        while not queue.empty():
            (curr, level) = queue.get()

            for i, c in enumerate(curr):
                for j in range(97, 123):
                    chg = curr[:i] + chr(j) + curr[i+1:]
                    if chg == endWord:
                        return level+1
                    elif chg in wordMap:
                        queue.put((chg, level+1))
                        # remove in map to prevent cyclic
                        del wordMap[chg]

        return 0

    def testLadder(self):
        self.assertEqual(0, self.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]))
        self.assertEqual(5, self.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
        self.assertEqual(4, self.ladderLength("lost", "miss", ["most","mist","miss","lost","fist","fish"]))
        self.assertEqual(6, self.ladderLength("leet", "code", ["lest","leet","lose","code","lode","robe","lost"]))
