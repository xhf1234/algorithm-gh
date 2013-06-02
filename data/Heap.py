#!/usr/bin/env python

""" DataStructure Heap """

from util.utils import swap

class Heap(object):
    """
    
    size
    extract_max()
    max()
    modify(index, value)
    insert(value)

    """
    size = None
    _list = None
    _cmp = None

    def __init__(self, cmp, list=None, size=None):
        """

        cmp, a compare function, if cmp(a, b)>0 then a will at the top of b
        list, init list data
        size, the real size of this heap, size<=len(list)

        """
        self._cmp = cmp
        if list is None:
            self._list = []
            self.size = 0
        else:
            self._list = list
            if size is None:
                size = len(self._list)
            self.size = size
            self._build_heap()

    def max(self):
        """ return the top element """
        if self.size == 0:
            return None
        return self._list[0]

    def extract_max(self):
        """ return and remove the top element """
        if self.size == 0:
            return None
        max = self._list[0]
        swap(self._list, 0, self.size-1)
        self.size = self.size-1
        if self.size > 1:
            self._down_heapify(0)
        return max

    def modify(self, index, value):
        """ set the new value to the element in the given index, use top_heapify or down_heapify to rebuild the heap """
        oldValue = self._list[index]
        self._list[index] = value
        if self._cmp(value, oldValue) > 0:
            self._top_heapify(index)
        elif self._cmp(value, oldValue) < 0:
            self._down_heapify(index)

    def insert(self, value):
        """ insert a new value and rebuild the heap """
        self._list.insert(self.size, value)
        self.size = self.size + 1
        self._top_heapify(self.size-1)

    def _build_heap(self):
        start = (self.size-1)/2
        for i in range(start, -1, -1):
            self._down_heapify(i)

    def _top_heapify(self, index):
        parent = (index-1)/2
        if parent>=0 and self._is_bigger(index, parent):
            swap(self._list, index, parent)
            self._top_heapify(parent)

    def _down_heapify(self, index):
        left = index*2+1
        right = left+1
        max = index
        if left<self.size and self._is_bigger(left, max):
            max = left
        if right<self.size and self._is_bigger(right, max):
            max = right 
        if max != index:
            swap(self._list, max, index)
            self._down_heapify(max)

    def _is_bigger(self, i, j):
        return self._cmp(self._list[i], self._list[j]) > 0


def _CMP_MIN(i, j):
    if i > j:
        return -1
    if i < j:
        return 1
    return 0


class MinHeap(Heap):

    def __init__(self, list=None, size=None):
        super(MinHeap, self).__init__(_CMP_MIN, list, size)


def _CMP_MAX(i, j):
    if i < j:
        return -1
    if i > j:
        return 1
    return 0


class MaxHeap(Heap):

    def __init__(self, list=None, size=None):
        super(MaxHeap, self).__init__(_CMP_MAX, list, size)


def main():
    list_ = [4,2,8,1,6,9,3,7,5, 0]
    heap = MaxHeap(list_)
    print 'max =', heap.max()
    heap.insert(10)
    print 'max =', heap.max()
    heap.modify(10, 11)
    print 'max =', heap.max()
    while heap.size != 0:
        print heap.extract_max()

if __name__ == '__main__':
    main()

