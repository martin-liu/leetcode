package com.martinliu.stringtointegeratoi;

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

        assertTrue(solution.atoi("-325") == -325);
        assertTrue(solution.atoi("+125") == 125);
        assertTrue(solution.atoi("  +125 ") == 125);
        assertTrue(solution.atoi("2147483648") == 2147483647);
        assertTrue(solution.atoi("    10522545459") == 2147483647);
        assertTrue(solution.atoi("-2147483648") == -2147483648);
    }
}
