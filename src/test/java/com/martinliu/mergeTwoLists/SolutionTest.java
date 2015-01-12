package com.martinliu.mergetwolists;

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

        ListNode l = new ListNode(1);
        l.next = new ListNode(3);
        l.next.next = new ListNode(5);
        ListNode ll = new ListNode(2);
        ll.next = new ListNode(4);
        ll.next.next = new ListNode(6);

        ListNode n = solution.mergeTwoLists(l, ll);
        assertTrue(n.next.val == 2);
        assertTrue(n.next.next.val == 3);
        assertTrue(n.next.next.next.val == 4);
        assertTrue(n.next.next.next.next.val == 5);
    }
}
