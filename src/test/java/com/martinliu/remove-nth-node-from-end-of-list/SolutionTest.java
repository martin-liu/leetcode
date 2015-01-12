package com.martinliu.removenthnodefromendoflist;

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

        ListNode head = new ListNode(1);
        head.next = new ListNode(2);
        head.next.next = new ListNode(3);
        head.next.next.next = new ListNode(4);
        head.next.next.next.next = new ListNode(5);

        assertTrue(solution.removeNthFromEnd(head, 2).next.next.next.val == 5);

        head = new ListNode(1);
        head.next = new ListNode(2);
        assertTrue(solution.removeNthFromEnd(head, 2).val == 2);
    }
}
