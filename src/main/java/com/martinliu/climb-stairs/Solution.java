package com.martinliu.climbstairs;
import java.util.*;

/**
   You are climbing a stair case. It takes n steps to reach to the top.

   Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
*/
public class Solution
{
    public int climbStairs(int n) {
        if (n == 1){
            return 1;
        } else if (n == 2) {
            return 2;
        } else {
            int l = 2;
            int ll = 1;
            for (int i = 3; i <= n; i++) {
                int tmp = l;
                l = l + ll;
                ll = tmp;
            }
            return l;
        }
    }
}
