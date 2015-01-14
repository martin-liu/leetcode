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
            // when terminal, if s equals "", means match
            return "".equals(s);
        } else {
            // simplify p
            p = convertP(p);
            String firstP = "";
            String restP = "";
            // prepare firstP and restP
            if (p.length() <= 1 ){
                firstP = p;
            } else if (p.charAt(1) == '*'){
                firstP = p.substring(0, 2);
                restP = p.substring(2, p.length());
            } else {
                firstP = p.substring(0, 1);
                restP = p.substring(1, p.length());
            }

            // try to match sub string
            String firstS = matchString(s, firstP);

            String restS = null;
            if (null == firstS){
                // match fail
                return false;
            } else if ("".equals(firstS)){
                // match ""
                restS = s;
            } else {
                restS = s.substring(firstS.length(), s.length());
            }

            return isMatch(restS, restP);
        }
    }

    // simplify p
    private String convertP(String p){
        int index = 0;
        int from = 0;
        while ((index = p.indexOf('*', from)) > -1){
            char c = p.charAt(index - 1);

        }
        return p;
    }

    // match sub String of s, match fail return null, no match return ""
    private String matchString(String s, String p){
        if (null != s && null != p){
            if (p.length() == 1){
                if (p.charAt(0) == '.' || s.indexOf(p) == 0){
                    if (s.length() > 0){
                        return s.substring(0, 1);
                    }
                }
            } else {
                // `p.length() == 2` => `x*` style
                if (".*".equals(p)){
                    return s;
                } else {
                    char first = p.charAt(0);
                    int i = 0;
                    while (i < s.length() && first == s.charAt(i)){
                        ++i;
                    }
                    return s.substring(0, i);
                }
            }
        }
        return null;
    }
}
