#!/usr/bin/env python
from permutation import perm

def comb(_list, k, cbk):
    n = len(_list)
    choose = []
    for i in range(k):
        choose.append(True)
    for i in range(n-k):
        choose.append(False)
    found = True
    while(found):
        rlist = []
        for i in range(n):
            if(choose[i]):
                rlist.append(_list[i])
        cbk(rlist)
        found = False
        for i in range(1, n):
            if (choose[i-1] and not choose[i]):
                found = True
                choose[i-1], choose[i] = False, True
                j,k = 0,i-2
                while j<k:
                    while j<k and choose[j]:
                        j = j+1
                    while j<k and not choose[k]:
                        k = k-1
                    if j<k:
                        choose[j], choose[k] = True, False
                        j, k = j+1, k-1
                break

if __name__ == '__main__':
    def cbk(_list):
        print _list
    def cbk_perm(_list):
        perm(_list, cbk)
    comb([1,2,3,4,5], 2, cbk_perm)

"""
recursive version

def __comb(_list, s, n, k, subset, cbk):
    if k == 0:
        cbk(subset)
        return
    if k > n:
        return
    if k == n:
        tlist = []
        tlist.extend(subset)
        tlist.extend(_list[s:s+k])
        cbk(tlist)
        return
    subset.append(_list[s])
    __comb(_list, s+1, n-1, k-1, subset, cbk)
    subset.remove(_list[s])
    __comb(_list, s+1, n-1, k, subset, cbk)

def comb(_list, k, cbk):
    __comb(_list, 0, len(_list), k, [], cbk)
"""
