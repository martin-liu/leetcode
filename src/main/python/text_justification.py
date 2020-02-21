import unittest
from typing import List

class Solution(unittest.TestCase):
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        """
Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.

Example 1:

Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Example 2:

Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be",
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified becase it contains only one word.
Example 3:

Input:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
        """

        wordLength = len(words)

        justifyLength = -1
        justifyAr = []
        justifyArLength = 0

        ret = []
        for n, word in enumerate(words):
            length = len(word)

            # add minimal one space length 1
            if justifyLength + 1 + length > maxWidth:
                extraSpace = maxWidth - justifyLength
                if justifyArLength == 1:
                    justifyAr[0] += ' ' * extraSpace
                else:
                    q, r = divmod(extraSpace, justifyArLength - 1)

                    for i in range(justifyArLength - 1):
                        justifyAr[i] += ' ' * q
                        if i < r:
                            justifyAr[i] += ' '

                ret.append(' '.join(justifyAr))

                # reset
                justifyLength = length
                justifyAr = [word]
                justifyArLength = 1
            else:
                justifyLength += 1 + length
                justifyAr.append(word)
                justifyArLength += 1

        if justifyAr:
            extraSpace = maxWidth - justifyLength
            justifyAr[-1] += ' ' * extraSpace
            ret.append(' '.join(justifyAr))

        return ret

    def testFullJustify(self):
        self.assertCountEqual(self.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16), ["This    is    an", "example  of text", "justification.  "])
        self.assertCountEqual(self.fullJustify(["What","must","be","acknowledgment","shall","be"], 16), ["What   must   be", "acknowledgment  ", "shall be        "])
        self.assertCountEqual(self.fullJustify(["Science","is","what","we","understand","well","enough","to","explain", "to","a","computer.","Art","is","everything","else","we","do"], 20), ["Science  is  what we", "understand      well", "enough to explain to", "a  computer.  Art is", "everything  else  we", "do                  "])
