### Data Structures for leetcode ###
###------------------------------###
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def toList(self):
        curr = self
        ret = [curr.val]
        while curr.next:
            ret.append(curr.next.val)
            curr = curr.next
        return ret

    @staticmethod
    def fromList(l):
        curr = None
        head = None
        for v in l:
            if not curr:
                curr = ListNode(v)
                head = curr
            else:
                curr.next = ListNode(v)
                curr = curr.next
        return head

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    # BFS
    def toList(self):
        queue = [self]
        ret = []
        while queue:
            tree = queue.pop(0)
            ret.append(tree.val if tree else None)
            if tree:
                queue.append(tree.left)
                queue.append(tree.right)

        i = 1
        while not ret[-i]:
            i += 1

        return ret[:-i+1]

    @staticmethod
    def fromList(l):
        if not l:
            return None
        length = len(l)

        for i, n in enumerate(l):
            if n is not None:
                node = TreeNode(n)
                q, r = divmod(i - 1, 2)

                if q >= 0:
                    if r == 0:
                        l[q].left = node
                    else:
                        l[q].right = node

                l[i] = node

        return l[0]
