package com.martinliu.removeelement;

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

        int[] A = {4, 5};
        assertTrue(solution.removeElement(A, 4) == 1);
        assertTrue(A[0] == 5);
    }
}
