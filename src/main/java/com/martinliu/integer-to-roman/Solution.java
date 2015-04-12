package com.martinliu.integertoroman;
import java.util.*;

/**
   Given an integer, convert it to a roman numeral.

   Input is guaranteed to be within the range from 1 to 3999.
*/
public class Solution
{
    private static Map<Integer, Character> map = new TreeMap<Integer, Character>(new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                return o2.compareTo(o1);
            }
        });

    static {
        map.put(1000, 'M');
        map.put(500, 'D');
        map.put(100, 'C');
        map.put(50, 'L');
        map.put(10, 'X');
        map.put(5, 'V');
        map.put(1, 'I');
    }

    public int getPrefix(int unit){
        int prefixInt = 0;
        if (unit == 1000 || unit == 500) {
            prefixInt = 100;
        } else if (unit == 100 || unit == 50) {
            prefixInt = 10;
        } else if (unit == 10 || unit == 5) {
            prefixInt = 1;
        }
        return prefixInt;
    }

    public String intToRoman(int num) {
        StringBuilder sb = new StringBuilder();
        for (Map.Entry<Integer, Character> entry : map.entrySet()) {
            int i = entry.getKey();
            char roman = entry.getValue();
            int div = num / i;
            int rem = num % i;

            for (int j = 0; j < div; j++) {
                sb.append(roman);
            }

            num = rem;

            // process prefix
            int in = getPrefix(i);
            if (0 != in) {
                // has prefix
                if (num >= i - in){
                    sb.append(map.get(in));
                    sb.append(roman);
                    num = num % in;
                }
            }
        }
        return sb.toString();
    }
}
