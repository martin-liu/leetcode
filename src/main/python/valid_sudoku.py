# 36. Valid Sudoku
# Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
# 1. Each row/column must have the numbers 1-9 occuring just once.
# 2. And the numbers 1-9 must occur just once in each of the 9 sub-boxes of the grid.

# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


# A partially filled sudoku which is valid.

# Note:
# A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.

# Basic idea: bitmap for each row/column/subbox
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        if not board:
            return False

        for i in range(len(board)):
            bitmapH = 0
            bitmapV = 0
            for j in range(len(board[i])):
                # row check
                if board[i][j] != '.':
                    bitmapH = self.checkBitmap(board[i][j], bitmapH)
                    if bitmapH == -1:
                        return False

                # column check
                if board[j][i] != '.':
                    bitmapV = self.checkBitmap(board[j][i], bitmapV)
                    if bitmapV == -1:
                        return False

                # sub box check
                if i % 3 == 0 and j % 3 == 0:
                    bitmap = 0
                    for k in range(i, i + 3):
                        for g in range(j, j + 3):
                            if board[k][g] != '.':
                                bitmap = self.checkBitmap(board[k][g], bitmap)
                                if bitmap == -1:
                                    return False

        return True

    def checkBitmap(self, char, bitmap):
        # each number use a bit
        # 1 -> 1, 2 -> 10, 3 -> 100, 4 -> 1000, ...
        num = 1 << (int(char) - 1)

        if num & bitmap == 0:
            # no duplicate
            # save to bitmap
            bitmap |= num

            return bitmap
        else:
            return -1

    # another way: use hash map to check duplication
    def isValidSudoku2(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        hash_table_row = {}
        hash_table_col = {}
        hash_table_block = {}
        m = len(board)
        n = len(board[0])

        for i in range(m):
            hash_table_row[i] = {}
            hash_table_col[i] = {}
            hash_table_block[i] = {}

        for i in range(m):
            for j in range(n):
                if board[i][j] == '.':
                    continue

                key = board[i][j]
                block = ((i//3) * 3) + (j//3)

                if key in hash_table_row[i] or key in hash_table_col[j] or key in hash_table_block[block]:
                    return False
                else:
                    hash_table_row[i][key] = True
                    hash_table_col[j][key] = True
                    hash_table_block[block][key] = True

        return True

# -----------------------------
import unittest

class Test(unittest.TestCase):
    def test(self):
        s = Solution()

        board = [
            ['.', '.', '.', '.', '5', '.', '.', '1', '.'],
            ['.', '4', '.', '3', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '3', '.', '.', '1'],
            ['8', '.', '.', '.', '.', '.', '.', '2', '.'],
            ['.', '.', '2', '.', '7', '.', '.', '.', '.'],
            ['.', '1', '5', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
            ['.', '2', '.', '9', '.', '.', '.', '.', '.'],
            ['.', '.', '4', '.', '.', '.', '.', '.', '.']
        ]
        self.assertFalse(s.isValidSudoku(board))

        board = [
            ['.', '.', '5', '.', '.', '.', '.', '.', '6'],
            ['.', '.', '.', '.', '1', '4', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '9', '2', '.', '.'],
            ['5', '.', '.', '.', '.', '2', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '3', '.'],
            ['.', '.', '.', '5', '4', '.', '.', '.', '.'],
            ['3', '.', '.', '.', '.', '.', '4', '2', '.'],
            ['.', '.', '.', '2', '7', '.', '6', '.', '.']
        ]
        self.assertTrue(s.isValidSudoku(board))

        board = [
            ['.', '.', '4', '.', '.', '.', '6', '3', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['5', '.', '.', '.', '.', '.', '.', '9', '.'],
            ['.', '.', '.', '5', '6', '.', '.', '.', '.'],
            ['4', '.', '3', '.', '.', '.', '.', '.', '1'],
            ['.', '.', '.', '7', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '5', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.']
        ]
        self.assertFalse(s.isValidSudoku(board))
