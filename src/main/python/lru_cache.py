import unittest

class DoubleLinkedNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

    def toList(self):
        curr = self
        ret = []
        while curr:
            ret.append(curr.val)
            curr = curr.next
        return ret

class LRUCache():
    """
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

---
Basic Idea: double linked hash map
"""

    def __init__(self, capacity: int):
        assert capacity > 0
        self.store = {}
        self.capacity = capacity
        self.count = 0
        self.head = DoubleLinkedNode(None, None)
        self.tail = DoubleLinkedNode(None, None)
        self.head.next, self.tail.prev = self.tail, self.head

    def get(self, key: int) -> int:
        cache = self.updateLRU(self.store.get(key))
        return cache.val if cache else -1

    def put(self, key: int, value: int) -> None:
        node = self.store.get(key, DoubleLinkedNode(key, value))
        node.val = value
        self.store[key] = self.updateLRU(node)

    def insertAfter(self, node, after):
        # `after.next.prev` must before `after.next`, otherwise `after.next` already changed
        after.next.prev, after.next, node.prev, node.next = node, node, after, after.next

    def cut(self, node):
        if node and node.prev and node.next:
            node.prev.next, node.next.prev = node.next, node.prev

    # make latest node as head
    def updateLRU(self, node):
        # ignore if change head
        if not node:
            return node

        # try cut node (if need)
        self.cut(node)

        # connect node to head
        self.insertAfter(node, self.head)

        # remove old node if exceed capacity
        if node.key not in self.store:
            # new node
            self.count += 1
            if self.count > self.capacity:
                del self.store[self.tail.prev.key]
                self.cut(self.tail.prev)
                self.count -= 1

        return node

class Tests(unittest.TestCase):
    def testLRU(self):
        cache = LRUCache(1)
        cache.put(2, 1)
        self.assertEqual(1, cache.get(2))
        cache.put(3, 2)
        self.assertEqual(-1, cache.get(2))
        self.assertEqual(2, cache.get(3))

        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        self.assertEqual(1, cache.get(1))
        cache.put(3, 3)    # evicts key 2
        self.assertEqual(-1, cache.get(2))
        cache.put(4, 4)    # evicts key 1
        self.assertEqual(-1, cache.get(1))
        self.assertEqual(3, cache.get(3))
        self.assertEqual(4, cache.get(4))

        cache = LRUCache(3)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.put(3, 3)
        cache.put(4, 4)    # evicts key 1
        self.assertEqual(4, cache.get(4))
        self.assertEqual(3, cache.get(3))
        self.assertEqual(2, cache.get(2))
        cache.put(5, 5)    # evicts key 4
        self.assertEqual(-1, cache.get(1))
        self.assertEqual(2, cache.get(2))
        self.assertEqual(3, cache.get(3))
        self.assertEqual(-1, cache.get(4))
        self.assertEqual(5, cache.get(5))
