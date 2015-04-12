package com.martinliu.threesum;

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

            int[] arr = {-1, 0, 1, 2, -1, -4};
            assertTrue(solution.threeSum(arr).toString().equals("[[-1, 0, 1], [-1, -1, 2]]"));
            assertTrue(solution.threeSum(new int[]{-2,-3,0,0,-2}).toString().equals("[]"));
            assertTrue(solution.threeSum(new int[]{-2,0,1,1,2}).toString().equals("[[-2, 1, 1], [-2, 0, 2]]"));
            assertTrue(solution.threeSum(new int[]{-1,1,0}).toString().equals("[[-1, 0, 1]]"));

            long startTime = System.nanoTime();
            solution.threeSum(new int[]{13,-5,3,3,-1,13,3,1,-9,-4,9,12,6,-9,-6,-12,-8,3,12,14,4,-15,2,-11,4,-12,10,9,-6,-3,-8,14,7,3,2,-8,-7,-10,8,-8,-7,-6,-11,6,-7,-2,9,-8,8,-2,13,-10,-2,0,-14,-13,-4,11,3,-3,-7,3,-4,8,13,13,-15,-9,10,0,-2,-12,1,2,9,1,8,-4,8,-7,9,7,-2,-15,14,0,-13,-13,-12,-2,-1,-11,8,10,12,6,8,4,12,3,11,-12,-2,-3,5,-15,6,-10,-4,-1,-1,-10,13});
            long endTime = System.nanoTime();

            long duration = (endTime - startTime);
            System.out.println("duration: " + duration / 1000000);

        }
}
