package com.martinliu.longestpalindromicsubstring;

import static org.junit.Assert.*;
import static org.mockito.Mockito.*;

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
        assertTrue(solution.longestPalindrome("aaaabaaa").equals("aaaabaaa"));
        assertTrue(solution.longestPalindrome("abcde").equals("a"));
        assertTrue(solution.longestPalindrome("abcbd").equals("bcb"));
        assertTrue(solution.longestPalindrome("abcdcbd").equals("bcdcb"));
        assertTrue(solution.longestPalindrome("bananas").equals("anana"));
        assertTrue(solution.longestPalindrome("ababababababa").equals("ababababababa"));
    }
}