package com.martinliu.removeduplicates;
import java.util.*;

/**
   Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

   Do not allocate extra space for another array, you must do this in place with constant memory.

   For example,
   Given input array A = [1,1,2],

   Your function should return length = 2, and A is now [1,2].
*/
public class Solution
{
    public int removeDuplicates(int[] A) {
        if (A == null || A.length == 0){
            return 0;
        }

        Map<Integer, Boolean> map = new HashMap<Integer, Boolean>();
        int curr = 0;
        for (int i = 0; i < A.length; i++) {
            if (map.get(A[i]) == null){
                A[curr++] = A[i];
                map.put(A[i], Boolean.TRUE);
            }
        }
        return curr;
    }
}
