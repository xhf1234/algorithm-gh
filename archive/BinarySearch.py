#!/usr/bin/env python

class SearchResult(object):
    def __init__(self, hit, index):
        self.hit = hit
        self.index = index

def search(tList, value, start=0, end=None):
    if end is None:
        end = len(tList)-1
    bottom,top = start,end
    while bottom <= top:
        mid = (bottom+top)/2
        midValue = tList[mid]
        if midValue == value:
            return SearchResult(True, mid)
        if midValue < value:
            bottom = mid+1
        else:
            top = mid - 1
    return SearchResult(False, bottom)
