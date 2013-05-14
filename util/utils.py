#!/usr/bin/env python
import random

def swap(list, i, j):
    t = list[i]
    list[i] = list[j]
    list[j] = t

def  randomList(n):
    tList = range(n)
    for i in range(n):
        k = random.randint(0, n-1)
        swap(tList, i, k)
    return tList
