#!/usr/bin/env python

from util.utils import randomList
from data.Heap import MaxHeap

def heap_sort(list):
    heap = MaxHeap(list)
    while heap.size != 0:
        heap.extract_min()

def main():
    tList = randomList(100)
    heap_sort(tList)
    print tList

if __name__ == '__main__':
    main()
