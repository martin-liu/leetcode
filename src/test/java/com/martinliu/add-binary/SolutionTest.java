package com.martinliu.addbinary;

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

        assertTrue(solution.addBinary("11", "1").equals("100"));
        assertTrue(solution.addBinary("11011", "1").equals("11100"));
    }
}
