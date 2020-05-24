import unittest

from heapq import heappop, heappush
class MedianFinder:
    """
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.


Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2


Follow up:

If all integer numbers from the stream are between 0 and 100, how would you optimize it?
If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?

---
Basic Idea: two heaps, one min heap, one max heap, maintain `[...,max] < [min,...]` and ensure `|len(max)-len(min)| <= 1`
"""

    def __init__(self):
        self.minH = []
        # for maxH, always do `-n` when push or pop, so that python's min heap implementation can represent max heap
        self.maxH = []

    def addNum(self, num: int) -> None:
        if not self.minH or num > self.minH[0]:
            heappush(self.minH, num)
        else:
            heappush(self.maxH, -num)

        diff = len(self.minH) - len(self.maxH)
        if diff > 1:
            n = heappop(self.minH)
            heappush(self.maxH, -n)
        elif diff < -1:
            n = - heappop(self.maxH)
            heappush(self.minH, n)

    def findMedian(self) -> float:
        if len(self.minH) == len(self.maxH):
            return (self.minH[0] - self.maxH[0]) / 2
        elif len(self.minH) > len(self.maxH):
            return self.minH[0]
        else:
            return -self.maxH[0]

class MedianFinder2:
    def __init__(self):
        self.minHeap = Heap(True)
        self.maxHeap = Heap(False)

    def addNum(self, num: int) -> None:
        if self.minHeap.size == 0 or self.minHeap.top() < num:
            self.minHeap.push(num)
        else:
            self.maxHeap.push(num)

        # balance 2 heaps
        diff = self.minHeap.size - self.maxHeap.size
        if diff > 1:
            self.maxHeap.push(self.minHeap.pop())
        elif diff < -1:
            self.minHeap.push(self.maxHeap.pop())

    def findMedian(self) -> float:
        if self.maxHeap.size == self.minHeap.size:
            return (self.maxHeap.top() + self.minHeap.top()) / 2
        elif self.maxHeap.size > self.minHeap.size:
            return self.maxHeap.top()
        else:
            return self.minHeap.top()

class Heap:
    def __init__(self, isMin = False):
        self.ar = []
        self.isMin = isMin
        self.size = 0

    def top(self):
        return self.ar[0] if self.ar else None

    # swap to end, delete end, then heapify(0) which swap with min/max child until valid
    def pop(self):
        if not self.ar:
            return None
        ar, isMin = self.ar, self.isMin
        first, last = ar[0], ar.pop()
        self.size -= 1
        if not ar:
            return first
        ar[0] = last

        p, l, r = 0, 1, 2
        tmpAr = [ar[i] for i in [p, l, r] if i < self.size]
        extremeNum = min(tmpAr) if isMin else max(tmpAr)
        while extremeNum != ar[p]:
            if extremeNum == ar[l]:
                ar[p], ar[l] = ar[l], ar[p]
                p, l, r = l, l*2+1, l*2+2
            else:
                ar[p], ar[r] = ar[r], ar[p]
                p, l, r = r, r*2+1, r*2+2
            tmpAr = [ar[i] for i in [p, l, r] if i < self.size]
            extremeNum = min(tmpAr) if isMin else max(tmpAr)
        return first

    # append, then swap with parent until valid
    def push(self, num:int):
        self.ar.append(num)
        self.size += 1
        i = self.size - 1
        p = (i-1) >> 1
        ar, isMin = self.ar, self.isMin
        while (isMin and p >= 0 and ar[p] > ar[i]) or (not isMin and p >= 0 and ar[p] < ar[i]):
            ar[i], ar[p] = ar[p], ar[i]
            i, p = p, (p-1) >> 1

class Tests(unittest.TestCase):
    def test(self):
        mf = MedianFinder()
        mf.addNum(12)
        mf.addNum(10)
        self.assertEqual(11, mf.findMedian())
        mf.addNum(13)
        self.assertEqual(12, mf.findMedian())
        mf.addNum(11)
        self.assertEqual(11.5, mf.findMedian())
        mf.addNum(5)
        self.assertEqual(11, mf.findMedian())
        mf.addNum(15)
        mf.addNum(1)
        mf.addNum(11)
        mf.addNum(6)
        mf.addNum(17)
        mf.addNum(14)
        self.assertEqual(11, mf.findMedian())
