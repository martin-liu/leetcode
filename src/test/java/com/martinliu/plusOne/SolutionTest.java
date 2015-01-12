package com.martinliu.plusone;

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

        int[] A = {1, 9, 9};
        int[] ret = solution.plusOne(A);
        assertTrue(ret[0] == 2);
        assertTrue(ret[1] == 0);

        A = new int[]{9, 9, 9};
        ret = solution.plusOne(A);
        assertTrue(ret[0] == 1);
        assertTrue(ret[3] == 0);
    }
}
