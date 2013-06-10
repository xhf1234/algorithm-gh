#!/usr/bin/env python
from util.utils import swap, randomList
import random

def quick_sort(tList):
    sort(tList, 0, len(tList)-1)

def sort(tList, start, end):
    if end-start <= 0:
        return
    pivot = partition(tList, start, end)
    sort(tList, start, pivot-1)
    sort(tList, pivot+1, end)

def partition(tList, start, end):
    p = random.randint(start, end)
    mValue = tList[p]
    swap(tList, start, p)
    i,j = start+1,end
    while i<=j:
        while i<=j and tList[i]<=mValue:
            i = i+1
        while i<=j and tList[j]>=mValue:
            j = j-1
        if i<j:
            swap(tList, i, j)
            i = i+1
            j = j-1
    p = i-1
    swap(tList, start, p)
    return p

def main():
    tList = randomList(100)
    quick_sort(tList)
    print tList

if __name__ == '__main__':
    main()
