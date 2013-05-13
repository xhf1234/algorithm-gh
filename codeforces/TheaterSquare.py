#!/usr/bin/env python
"""
    http://codeforces.com/problemset/problem/1/A
"""

if __name__ == '__main__':
    n, m, a = [int(x) for x in raw_input().split()]
    w = n/a
    if n%a != 0:
        w = w + 1
    h = m/a
    if m%a != 0:
        h = h + 1
    print w*h
