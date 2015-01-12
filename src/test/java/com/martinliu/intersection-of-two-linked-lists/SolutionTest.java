package com.martinliu.intersectionoftwolinkedlists;

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

        ListNode A = new ListNode(1);
        A.next = new ListNode(2);
        ListNode B = new ListNode(11);
        B.next = new ListNode(2);
        assertTrue(solution.getIntersectionNode(A, B) == null);

        A = new ListNode(1);
        A.next = new ListNode(2);
        B = new ListNode(11);
        B.next = A.next;
        assertTrue(solution.getIntersectionNode(A, B) == A.next);
    }
}
