package com.martinliu.countandsay;

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

        assertTrue(solution.countAndSay(2).equals("11"));
        assertTrue(solution.countAndSay(3).equals("21"));
        assertTrue(solution.countAndSay(4).equals("1211"));
        assertTrue(solution.countAndSay(5).equals("111221"));
    }
}
