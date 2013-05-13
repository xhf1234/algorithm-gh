#!/usr/bin/env python
from util.utils import swap

def perm(tList, cbk, start=None, end=None):
    """
        generate the permutation of tList, for each list in the permutation result,
        call cbk(list)
        start is the first index, None means 0
        end is the last index, None means len(tList)-1
    """
    if start is None:
        start = 0
    if end is None:
        end = len(tList)-1
    if start>=end:
        cbk(tList)
        return
    for i in range(start, end+1):
        swap(tList, start, i)
        perm(tList, cbk, start+1, end)
        swap(tList, start, i)

def sort(tList):
    for j in range(len(tList)-1, 0, -1):
        for i in range(1, j+1):
            if tList[i] < tList[i-1]:
                swap(tList, i, i-1)

def perm_interactive(tList, cbk):
    if len(tList) <= 1:
        cbk(tList)
        return
    sort(tList)
    flags = [False] * len(tList)
    def left(i):
        return not flags[i]
    def active(i):
        if left(i) and i>0 and tList[i]>tList[i-1]:
            return True
        if not left(i) and i<len(tList)-1 and tList[i]>tList[i+1]:
            return True
        return False
    def turn(i):
        flags[i] = not flags[i]
    def exchange(i, j):
        swap(tList, i, j)
        swap(flags, i, j)
    max = -1 #index of the max active element
    while True:
        cbk(tList)
        if max is -1:
            for i in range(0, len(tList)):
                if max is -1 or tList[i]>tList[max]:
                    if active(i):
                        max = i
        if max is -1:
            break
        if left(max):
            exchange(max, max-1)
            max = max-1
        else:
            exchange(max, max+1)
            max = max+1
        newMax = max
        for i in range(0, len(tList)):
            if tList[i] > tList[max]:
                turn(i)
                if tList[i]>tList[newMax] and active(i):
                    newMax = i
        max = newMax
        if not active(max):
            max = -1

def main():
    tList = [3, 1, 2]
    def cbk(tList):
        print tList
    perm_interactive(tList, cbk)

if __name__ == '__main__':
    main()
