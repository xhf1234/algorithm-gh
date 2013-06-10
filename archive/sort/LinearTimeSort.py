#!/usr/bin/env python

from util.utils import randomList_duplicate, randomList
import math
from SimpleSort import insert_sort as sort

def counting_sort(list_, MAX):
    if not list_:
        return
    c = [0]*(MAX+1)
    for e in list_:
        c[e] += 1
    for i in range(1, len(c)):
        c[i] += c[i-1]
    b = list_[:]
    for e in b:
        list_[c[e]-1] = e
        c[e] -= 1

def bitmap_sort(list_, MAX):
    if not list_:
        return
    bitmap = [0] * (MAX+1)
    for e in list_:
        bitmap[e] = 1
    i = 0
    for j,e in enumerate(bitmap):
        if e is 1:
            list_[i] = j
            i += 1

def radix_sort(list_, digits, base):
    def get_digit(value, d):
        return (value//base**(d-1))%base
    def d_sort(d):
        buckets = [[] for i in range(base)]
        for value in list_:
            digit = get_digit(value, d)
            buckets[digit].append(value)
        m = 0
        for bucket in buckets:
            for value in bucket:
                list_[m] = value
                m += 1
    for d in range(1, digits+1):
        d_sort(d)

def bucket_sort(list_):
    bucket_size = int(math.sqrt(len(list_)))
    buckets = [[] for _ in range(bucket_size)]
    m = max(list_)
    def hash(e):
        return int(e/m*(bucket_size-1))
    for e in list_:
        h = hash(e)
        buckets[h].append(e)
    for bucket in buckets:
        sort(bucket)
    i = 0
    for bucket in buckets:
        for e in bucket:
            list_[i] = e
            i += 1

def main():
    MAX = 24
    list_ = randomList_duplicate(100, MAX)
    bucket_sort(list_)
    print list_

if __name__ == '__main__':
    main()
