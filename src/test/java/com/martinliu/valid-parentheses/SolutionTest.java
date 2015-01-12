package com.martinliu.validparentheses;

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

        assertTrue(solution.isValid("()"));
        assertTrue(solution.isValid("([{}])"));
        assertFalse(solution.isValid("([{}}])"));
    }
}
