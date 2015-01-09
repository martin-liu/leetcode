package com.martinliu.removeduplicates;

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

        int[] A = {1, 1, 2};
        assertTrue(solution.removeDuplicates(A) == 2);
        assertTrue(A[1] == 2);
    }
}
