#!/usr/bin/env python
from utils import swap

def __perm(_list, s, e, callback):
    if s >= e:
        callback(_list)
    else:
        for i in range(s, e+1):
            swap(_list, s, i)
            __perm(_list, s+1, e, callback)
            swap(_list, s, i)

def perm(_list, callback):
    """ calculate all the permutation of _list and call callback(result_list) """
    __perm(_list, 0, len(_list)-1, callback)

if __name__ == '__main__':
    _list = [1, 2, 3, 4, 5]
    def callback(_list):
        print _list
    perm(_list, callback)
