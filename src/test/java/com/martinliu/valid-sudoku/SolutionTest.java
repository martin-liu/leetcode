package com.martinliu.validsudoku;

import static org.junit.Assert.*;

import java.util.*;
import org.junit.Test;
import org.junit.Ignore;
import org.junit.runner.RunWith;
import org.junit.runners.JUnit4;

/**
 * Unit test for Solution.
 */
public class SolutionTest {
    @Test
    public void test()
    {
        Solution solution = new Solution();

        char[][] board = new char[9][9];
        board[0] = new char[]{'.', '.', '.', '.', '5', '.', '.', '1', '.'};
        board[1] = new char[]{'.', '4', '.', '3', '.', '.', '.', '.', '.'};
        board[2] = new char[]{'.', '.', '.', '.', '.', '3', '.', '.', '1'};
        board[3] = new char[]{'8', '.', '.', '.', '.', '.', '.', '2', '.'};
        board[4] = new char[]{'.', '.', '2', '.', '7', '.', '.', '.', '.'};
        board[5] = new char[]{'.', '1', '5', '.', '.', '.', '.', '.', '.'};
        board[6] = new char[]{'.', '.', '.', '.', '.', '2', '.', '.', '.'};
        board[7] = new char[]{'.', '2', '.', '9', '.', '.', '.', '.', '.'};
        board[8] = new char[]{'.', '.', '4', '.', '.', '.', '.', '.', '.'};
        //assertFalse(solution.isValidSudoku(board));

        board = new char[9][9];
        board[0] = new char[]{'.', '.', '5', '.', '.', '.', '.', '.', '6'};
        board[1] = new char[]{'.', '.', '.', '.', '1', '4', '.', '.', '.'};
        board[2] = new char[]{'.', '.', '.', '.', '.', '.', '.', '.', '.'};
        board[3] = new char[]{'.', '.', '.', '.', '.', '9', '2', '.', '.'};
        board[4] = new char[]{'5', '.', '.', '.', '.', '2', '.', '.', '.'};
        board[5] = new char[]{'.', '.', '.', '.', '.', '.', '.', '3', '.'};
        board[6] = new char[]{'.', '.', '.', '5', '4', '.', '.', '.', '.'};
        board[7] = new char[]{'3', '.', '.', '.', '.', '.', '4', '2', '.'};
        board[8] = new char[]{'.', '.', '.', '2', '7', '.', '6', '.', '.'};
        assertTrue(solution.isValidSudoku(board));
    }
}
