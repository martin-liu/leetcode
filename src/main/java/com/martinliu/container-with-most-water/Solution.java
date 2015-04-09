package com.martinliu.containerwithmostwater;
import java.util.*;

/**
   Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

   Note: You may not slant the container.
*/
public class Solution
{
    public int maxArea(int[] height) {
        int len = height.length;
        if (len < 2){
            return 0;
        } else if (len == 2) {
            return Math.min(height[0], height[1]);
        } else {
            int maxArea = 0;
            int left = 0;
            int right = len - 1;

            while (left < right) {
                int min = Math.min(height[left], height[right]);
                int area = (right - left) * min;
                if (area > maxArea) {
                    maxArea = area;
                }

                // The max area is determined by the min
                // if next is small than min, then it will never get bigger area
                while (left < len && height[left] <= min) {
                    left++;
                }
                while (right > 0 && height[right] <= min) {
                    right--;
                }
            }
            return maxArea;
        }
    }
}
