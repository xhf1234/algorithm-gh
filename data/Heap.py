#!/usr/bin/env python
from util import utils

class Heap(object):

    def __init__(self, cmp, list=None):
        self._cmp = cmp
        if list is not None:
            self._list = list
            self._createHeap()
        else:
            self._list = []

    def min(self):
        if self.size() == 0:
            return -1
        return self._list[0]

    def insert(self, value):
        self._list.append(value)
        index = self.size()-1
        parent = self._getParent(index)
        while parent>=0 and self._lessThan(parent, index):
            utils.swap(self._list, parent, index)
            index = parent
            parent = self._getParent(index)

    def size(self):
        return len(self._list)

    def _createHeap(self):
        for i in range((self.size()-1)/2, -1, -1):
            self._heapify(i)

    def _getParent(self, index):
        if index%2 == 0:
            return index/2-1
        return index/2
    
    def _heapify(self, index):
        left = 2*index + 1
        right = 2*index + 2
        min = index
        size = self.size()
        if (left<size and self._lessThan(left, min)):
            min = left
        if (right<size and self._lessThan(right, min)):
            min = right
        if (min != index):
            utils.swap(self._list, min, index)
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

def main():
    tList = [4,2,8,1,6,9,3,7,5, 0]
    heap = MinHeap(tList)
    print 'min =', heap.min()
