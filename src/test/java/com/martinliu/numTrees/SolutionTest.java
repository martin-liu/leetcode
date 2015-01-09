package com.martinliu.numtrees;

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

        assertTrue(solution.numTrees(1) == 1);
        assertTrue(solution.numTrees(2) == 2);
        assertTrue(solution.numTrees(3) == 5);
    }
}
