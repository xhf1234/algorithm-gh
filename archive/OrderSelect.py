#!/usr/bin/env python

from archive.sort.QuickSort import partition
from util.utils import randomList

def randomized_select(list_, start, end, i):
    if start>end or i<0 or i>end-start:
        print start,end,i
        print 'error'
        return
    if start == end:
        return list_[start]
    pivot = partition(list_, start, end)
    if pivot == start+i:
        return list_[pivot]
    if start+i > pivot:
        return randomized_select(list_, pivot+1, end, start+i-pivot-1)
    else:
        return randomized_select(list_, start, pivot-1, i)

def order_select(list_, i):
    return randomized_select(list_, 0, len(list_)-1, i)

def main():
    list_ = randomList(100)
    print order_select(list_, 34)

if __name__ == '__main__':
    main()
