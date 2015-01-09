package com.martinliu.singlenumber;

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

        for (int i = 0; i < 100; i++) {
            Random r = new Random();
            int num = r.nextInt(100) + 1;

            int[] nums = new int[num * 2 + 1];
            for (int j = 0; j < num; j++) {
                int rr = r.nextInt();
                nums[j] = rr;
                nums[nums.length - 2 - j] = rr;
            }
            int a = r.nextInt();
            nums[num * 2] = a;
            assertTrue(solution.singleNumber(nums) == a);
        }
    }
}
