package com.martinliu.threesumclosest;
import java.util.*;

/**
   Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

   For example, given array S = {-1 2 1 -4}, and target = 1.

   The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

*/
public class Solution
{
    // Basic idea: find 2sum in rest of the array based on head
    public int threeSumClosest(int[] num, int target) {
        int closest = num[0] + num[1] + num[2];
        for (int i = 0; i < num.length - 2; i++) {
            for (int j = i + 1; j < num.length - 1; j++) {
                for (int k = j + 1; k < num.length; k++) {
                    int sum = num[i] + num[j] + num[k];

                    if (Math.abs(target - sum) < Math.abs(target - closest)) {
                        closest = sum;
                        System.out.println(num[i] + ", " + num[j] + ", " + num[k]);
                    }
                }
            }

        }

        System.out.println(closest);

        return closest;
    }
}
