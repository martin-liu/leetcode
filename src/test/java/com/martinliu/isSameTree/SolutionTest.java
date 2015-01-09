package com.martinliu.issametree;

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

        TreeNode p = new TreeNode(1);
        p.left = new TreeNode(2);
        p.right = new TreeNode(2);

        TreeNode q = new TreeNode(1);
        q.left = new TreeNode(2);
        q.right = new TreeNode(2);

        assertTrue(solution.isSameTree(p, q));

        TreeNode pp = new TreeNode(1);
        pp.left = new TreeNode(2);
        pp.right = new TreeNode(2);

        TreeNode qq = new TreeNode(1);
        qq.left = new TreeNode(2);

        assertFalse(solution.isSameTree(pp, qq));
    }
}
