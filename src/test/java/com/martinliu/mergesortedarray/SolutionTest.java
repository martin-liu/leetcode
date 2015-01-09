package com.martinliu.mergesortedarray;

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

        int[] A = {1, 3, 5, 0, 0, 0};
        int[] B = {2, 4, 6};
        solution.merge(A, 3, B, 3);
        assertTrue(A.length == 6);
        assertTrue(A[1] == 2);
        assertTrue(A[3] == 4);
    }
}
