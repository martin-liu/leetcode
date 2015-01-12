package com.martinliu.stringtointegeratoi;
import java.util.*;

/**
   Implement atoi to convert a string to an integer.

   Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

   Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

   Requirements for atoi:
   The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

   The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

   If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

   If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
*/
public class Solution
{
    public int atoi(String s) {
        if (null != s){
            char[] chars = s.toCharArray();
            boolean negative = false;
            int start = 0;

            // ignore space and check if negative
            for (int i = 0; i < chars.length; i++) {
                char c = chars[i];
                if (c == ' '){
                    continue;
                } else {
                    if (c == '-' || c == '+'){
                        if (c == '-'){
                            negative = true;
                        }
                        start = i + 1;
                    } else {
                        start = i;
                    }
                    break;
                }
            }

            int ret = 0;
            for (int i = start; i < chars.length; i++) {
                int num = charToInt(chars[i]);
                if (num == -1){
                    break;
                } else {
                    // check overflow
                    if (!negative){
                        if ((Integer.MAX_VALUE - num)/10 >= ret){
                            ret = ret * 10 + num;
                        } else {
                            ret = Integer.MAX_VALUE;
                        }
                    } else {
                        // minus 1 to prevent overflow
                        if ((Integer.MIN_VALUE + num)/10 <= ret){
                            ret = ret * 10 - num;
                        } else {
                            ret = Integer.MIN_VALUE;
                        }
                    }
                }
            }
            return ret;
        }
        return 0;
    }

    private int charToInt(char c){
        char[] arr = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};
        for (int i = 0; i < arr.length; i++) {
            if (c == arr[i]){
                return i;
            }
        }
        return -1;
    }
}
