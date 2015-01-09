package com.martinliu.zigzagconversion;

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

        assertTrue(solution.convert("PAYPALISHIRING", 3).equals("PAHNAPLSIIGYIR"));
        assertTrue(solution.convert("ABC", 2).equals("ACB"));
        assertTrue(solution.convert("ABCD", 2).equals("ACBD"));
        assertTrue(solution.convert("A", 1).equals("A"));
    }
}
