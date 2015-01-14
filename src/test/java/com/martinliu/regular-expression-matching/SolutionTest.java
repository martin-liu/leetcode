package com.martinliu.regularexpressionmatching;

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

        assertFalse(solution.isMatch("aa", "a"));
        assertFalse(solution.isMatch("aaa", "aa"));
        assertFalse(solution.isMatch("a", ".*..a*"));
        assertFalse(solution.isMatch("ab", ".*c"));
        assertFalse(solution.isMatch("aaba", "ab*a*c*a"));

        assertTrue(solution.isMatch("aa", "aa"));
        assertTrue(solution.isMatch("aa", "a*"));
        assertTrue(solution.isMatch("aa", ".*"));
        assertTrue(solution.isMatch("ab", ".*"));
        assertTrue(solution.isMatch("aab", "c*a*b*"));
        assertTrue(solution.isMatch("aab", "c*a*b*d*"));
        assertTrue(solution.isMatch("aaa", "a*a"));
        assertTrue(solution.isMatch("ab", ".*.."));
    }
}
