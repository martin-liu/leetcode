package com.martinliu.threesum;
import java.util.*;

/**
   Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

   Note:
   Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
   The solution set must not contain duplicate triplets.
   For example, given array S = {-1 0 1 2 -1 -4},

   A solution set is:
   (-1, 0, 1)
   (-1, -1, 2)
*/
public class Solution
{
    // Basic idea: find 2sum in rest of the array based on head
    public List<List<Integer>> threeSum(int[] num) {
        List<List<Integer>> list = new ArrayList<List<Integer>>();
        int len = num.length;
        if (len >= 3) {
            Map<Integer, Boolean> visit = new HashMap<Integer, Boolean>();
            for (int i = 0; i < len; i++) {
                // prevent duplicate
                if (visit.get(num[i]) == null){
                    Map<Integer, Integer> map = new HashMap<Integer, Integer>();
                    Map<Integer, Boolean> v = new HashMap<Integer, Boolean>();
                    int sum = - num[i];
                    for (int j = i + 1; j < len; j++) {
                        Integer n = map.get(num[j]);
                        int diff = sum - num[j];
                        // outer loop will cover num[i], num[j] and diff
                        if (visit.get(num[j]) == null && visit.get(diff) == null){
                            if (n == null) {
                                map.put(diff, num[j]);
                            }
                            // if find and not visit in this loop
                            else if (null == v.get(num[j])){
                                list.add(buildSolutionSet(num[i], n, num[j]));
                                v.put(num[j], true);
                            }
                        }
                    }
                    visit.put(num[i], true);
                }
            }
        }

        return list;
    }

    private List<Integer> buildSolutionSet(int left, int mid, int right) {
        List<Integer> list = new ArrayList<Integer>();
        list.add(left);
        list.add(mid);
        list.add(right);
        Collections.sort(list);
        return list;
    }
}
