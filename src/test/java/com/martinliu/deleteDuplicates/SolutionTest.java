package com.martinliu.deleteduplicate;

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
        head.next = new ListNode(1);
        head.next.next = new ListNode(2);

        assertTrue(solution.deleteDuplicates(head).next.val == 2);
        assertTrue(solution.deleteDuplicates(null) == null);

        head.next = new ListNode(1);
        head.next.next = new ListNode(1);
        assertTrue(solution.deleteDuplicates(head).next == null);
    }
}
