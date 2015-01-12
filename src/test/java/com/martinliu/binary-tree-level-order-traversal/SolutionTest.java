package com.martinliu.levelorder;

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

        TreeNode root = new TreeNode(3);
        root.left = new TreeNode(9);
        root.right = new TreeNode(20);
        root.right.left = new TreeNode(15);
        root.right.right = new TreeNode(7);

        List<List<Integer>> l = solution.levelOrder(root);

        assertTrue(l.get(0).get(0) == 3);
        assertTrue(l.get(1).get(0) == 9);
        assertTrue(l.get(2).get(1) == 7);
    }
}
