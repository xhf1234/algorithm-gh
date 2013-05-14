#!/usr/bin/env python

from util.utils import swap, randomList
from BinarySearch import search

def select_sort(tList):
    if tList is None or len(tList) is 0:
        return
    for i in range(1, len(tList)):
        min = i-1
        for j in range(i, len(tList)):
            if tList[j] < tList[min]:
                min = j
        swap(tList, i-1, min)

def insert_sort(tList):
    if tList is None or len(tList) is 0:
        return
    for i in range(1, len(tList)):
        t = tList[i]
        for j in range(i-1, -1, -1):
            if tList[j]>t:
                tList[j+1] = tList[j]
            else:
                tList[j+1] = t
                break
        else:
            tList[0] = t

def binary_insert_sort(tList):
    if tList is None or len(tList) is 0:
        return
    for i in range(1, len(tList)):
        t = tList[i]
        idx = search(tList, t, 0, i-1).index
        for j in range(i, idx, -1):
            tList[j] = tList[j-1]
        tList[idx] = t

def bubble_sort(tList):
    if tList is None or len(tList) is 0:
        return
    for i in range(len(tList)-1, 0, -1):
        exchange = False
        for j in range(1, i+1):
            if tList[j] < tList[j-1]:
                swap(tList, j, j-1)
                exchange = True
        if not exchange:
            break

def main():
    tList = randomList(100)
    bubble_sort(tList)
    print tList

if __name__ == '__main__':
    main()

