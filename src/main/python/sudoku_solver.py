import unittest

class Solution(unittest.TestCase):
    def solveSudoku(self, board):
        """
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

   Each of the digits 1-9 must occur exactly once in each row.
   Each of the digits 1-9 must occur exactly once in each column.
   Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
   Empty cells are indicated by the character '.'.

Note:
   The given board contain only digits 1-9 and the character '.'.
   You may assume that the given Sudoku puzzle will have a single unique solution.
   The given board size is always 9x9.
  """

    def solveSudoku(self, board):
        self.travel(0, 0, board)

    # Basic idea: recursively update and check, if next cells have conflict, revert the update
    def travel(self, i, j, board):
        if j >= 9:
            # next line
            return self.travel(i + 1, 0, board)
        if i == 9:
            # finish
            return True

        if board[i][j] == ".":
            for num in range(1, 10):
                num_str = str(num)
                if all(
                    # not in whole row
                    [board[i][col] != num_str for col in range(9)]
                ) and all(
                    # not in whole col
                    [board[row][j] != num_str for row in range(9)]
                ) and all(
                    # not in whole block
                    [board[i // 3 * 3 + count // 3][j // 3 * 3 + count % 3] != num_str for count in range(9)]
                ):
                    # update num to board
                    board[i][j] = num_str
                    # check next cells
                    if not self.travel(i, j + 1, board):
                        # revert if next cells found conflict
                        # travel changes will recursively revert
                        board[i][j] = "."
                    else:
                        return True
        else:
            # skip current cell
            return self.travel(i, j + 1, board)

        return False

    def test(self):
        s = Solution()
        board = [
            ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
            ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
            ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
            ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
            ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
            ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
            ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
            ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
            ['.', '.', '.', '.', '8', '.', '.', '7', '9']
        ]
        expectedBoard = [
            ['5', '3', '4', '6', '7', '8', '9', '1', '2'],
            ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
            ['1', '9', '8', '3', '4', '2', '5', '6', '7'],
            ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
            ['4', '2', '6', '8', '5', '3', '7', '9', '1'],
            ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
            ['9', '6', '1', '5', '3', '7', '2', '8', '4'],
            ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
            ['3', '4', '5', '2', '8', '6', '1', '7', '9']
        ]

        s.solveSudoku(board)
        self.assertEqual(board, expectedBoard)
