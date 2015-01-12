package com.martinliu.pascalstriangleii;

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

        assertEquals(solution.getRow(1).toString(), "[1, 1]");
        assertEquals(solution.getRow(2).toString(), "[1, 2, 1]");
        assertEquals(solution.getRow(3).toString(), "[1, 3, 3, 1]");
    }
}
