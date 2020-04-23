### Data Structures for leetcode ###
###------------------------------###
from queue import Queue

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
        queue = Queue()
        queue.put(self)
        ret = []
        while not queue.empty():
            tree = queue.get()
            ret.append(tree.val if tree else None)
            if tree:
                queue.put(tree.left)
                queue.put(tree.right)

        i = 1
        while not ret[-i]:
            i += 1

        return ret[:-i+1]

    @staticmethod
    def fromList(l):
        if not l:
            return None
        length = len(l)

        root = TreeNode(l[0])
        queue = Queue()
        queue.put(root)
        i = 1
        while not queue.empty() and i < length:
            curr = queue.get()
            if l[i] is not None:
                curr.left = TreeNode(l[i])
                queue.put(curr.left)
            i += 1
            if i < length and l[i] is not None:
                curr.right = TreeNode(l[i])
                queue.put(curr.right)
            i += 1

        return root

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    @staticmethod
    def fromList(l):
        if not l:
            return None
        length = len(l)

        for i, n in enumerate(l):
            if n is not None:
                node = Node(n)
                q, r = divmod(i - 1, 2)

                if q >= 0:
                    if r == 0:
                        l[q].left = node
                    else:
                        l[q].right = node

                l[i] = node

        return l[0]
