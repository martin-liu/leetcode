package com.martinliu.integertoroman;

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

        assertEquals(solution.intToRoman(1954), "MCMLIV");
        assertEquals(solution.intToRoman(1990), "MCMXC");
        assertEquals(solution.intToRoman(2014), "MMXIV");
        assertEquals(solution.intToRoman(2414), "MMCDXIV");
    }
}
