package com.martinliu.regularexpressionmatching;
import java.util.*;

/**
   Implement regular expression matching with support for '.' and '*'.

   '.' Matches any single character.
   '*' Matches zero or more of the preceding element.

   The matching should cover the entire input string (not partial).

   The function prototype should be:
   bool isMatch(const char *s, const char *p)

   Some examples:
   isMatch("aa","a") → false
   isMatch("aa","aa") → true
   isMatch("aaa","aa") → false
   isMatch("aa", "a*") → true
   isMatch("aa", ".*") → true
   isMatch("ab", ".*") → true
   isMatch("aab", "c*a*b") → true
*/
public class Solution
{
    public boolean isMatch(String s, String p) {
        // null check
        if (s == null || p == null){
            return false;
        }
        // terminal of recursion
        else if ("".equals(p)){
            return "".equals(s);
        } else if ("".equals(s) && !p.endsWith("*")){
            return false;
        } else {
            if (p.endsWith("*")) {
                return starMatch(s, p);
            } else if (p.endsWith(".") || equalsLast(s, p)) {
                return isMatch(removeLast(s, 1), removeLast(p, 1));
            } else {
                return false;
            }
        }
    }

    private String removeLast(String s, int n) {
        if (s == null || n > s.length()){
            return s;
        }
        String ret = s.substring(0, s.length() - n);
        if (ret == null){
            ret = "";
        }
        return ret;
    }

    private boolean equalsLast(String s1, String s2) {
        char c1 = s1.charAt(s1.length() - 1);
        char c2 = s2.charAt(s2.length() - 1);
        return c1 == c2;
    }

    private boolean matchLast(String s, char c){
        if (s == null || "".equals(s)){
            return false;
        }
        return c == '.' || s.charAt(s.length() - 1) == c;
    }

    private boolean starMatch(String s, String p){
        char pre = p.charAt(p.length() - 2);
        p = removeLast(p, 2);

        if (isMatch(s, p)){
            return true;
        }

        while (matchLast(s, pre)) {
            s = removeLast(s, 1);
            if (isMatch(s, p)){
                return true;
            }
        }
        return false;
    }
}
