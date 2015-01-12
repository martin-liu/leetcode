package com.martinliu.palindromenumber;

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

        assertTrue(solution.isPalindrome(1));
        assertFalse(solution.isPalindrome(12));
        assertTrue(solution.isPalindrome(121));
    }
}
