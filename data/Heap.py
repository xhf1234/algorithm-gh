#!/usr/bin/env python
from util.utils import swap

class Heap(object):
    size = None

    def __init__(self, cmp, list=None, size=None):
        self._cmp = cmp
        if list is not None:
            self._list = list
            if size is None:
                size = len(list)
            self.size = size
            self._createHeap()
        else:
            self._list = []
            self.size = 0

    def extract_min(self):
        if self.size == 0:
            return None
        swap(self._list, 0, self.size-1)
        self.size = self.size-1
        self._heapify(0)
        return self._list[self.size]

    def insert(self, value):
        index = self.size
        self._list.insert(index, value)
        self.size = self.size + 1
        parent = self._getParent(index)
        while parent>=0 and self._lessThan(index, parent):
            swap(self._list, parent, index)
            index = parent
            parent = self._getParent(index)

    def _createHeap(self):
        for i in range((self.size-1)/2, -1, -1):
            self._heapify(i)

    def _getParent(self, index):
        return (index-1)/2
    
    def _heapify(self, index):
        left = 2*index + 1
        right = 2*index + 2
        min = index
        size = self.size
        if (left<size and self._lessThan(left, min)):
            min = left
        if (right<size and self._lessThan(right, min)):
            min = right
        if (min != index):
            swap(self._list, min, index)
            self._heapify(min)

    def _lessThan(self, i, j):
        return self._cmp(self._list[i], self._list[j]) < 0

class MinHeap(Heap):
    def __init__(self, list=None):
        def cmp(u, v):
            if u<v:
                return -1
            if u>v:
                return 1
            return 0
        super(MinHeap, self).__init__(cmp, list)

class MaxHeap(Heap):
    def __init__(self, list=None):
        def cmp(u, v):
            if u>v:
                return -1
            if u<v:
                return 1
            return 0
        super(MaxHeap, self).__init__(cmp, list)

def main():
    tList = [4,2,8,1,6,9,3,7,5, 0]
    heap = MinHeap(tList)
    while heap.size != 0:
        print heap.extract_min()
