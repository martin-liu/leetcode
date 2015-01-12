package com.martinliu.longestpalindromicsubstring;

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

        assertTrue(solution.longestPalindrome("aaaa").equals("aaaa"));
        assertTrue(solution.longestPalindrome("aaaabaaa").equals("aaabaaa"));
        assertTrue(solution.longestPalindrome("abcbd").equals("bcb"));
        assertTrue(solution.longestPalindrome("abcdcbd").equals("bcdcb"));
        assertTrue(solution.longestPalindrome("bananassa").equals("anana"));
        assertTrue(solution.longestPalindrome("ababababababa").equals("ababababababa"));
    }
}
