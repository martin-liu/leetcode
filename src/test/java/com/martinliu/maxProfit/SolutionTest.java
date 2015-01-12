package com.martinliu.maxprofit;

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

        int[] p = {};
        assertTrue(solution.maxProfit(p) == 0);

        p = new int[]{1, 2};
        assertTrue(solution.maxProfit(p) == 1);

        p = new int[]{1, 2, 3};
        assertTrue(solution.maxProfit(p) == 2);

        p = new int[]{2, 3, 1};
        assertTrue(solution.maxProfit(p) == 1);

        p = new int[]{2, 3, 1, 2};
        assertTrue(solution.maxProfit(p) == 2);
    }
}
