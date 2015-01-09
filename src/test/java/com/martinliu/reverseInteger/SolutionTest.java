package com.martinliu.reverseinteger;

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

        assertTrue(solution.reverse(-103) == -301);
        assertTrue(solution.reverse(132) == 231);
        assertTrue(solution.reverse(130) == 31);
        // overflow
        assertTrue(solution.reverse(1000000003) == 0);
    }
}
