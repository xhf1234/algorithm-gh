#!/usr/bin/env python

class Queue(object):
    def __init__(self):
        self._list = []

    def enqueue(self, x):
        self._list.append(x)

    def dequeue(self):
        if self.size() > 0:
            return self._list.pop(0)
        return None

    def popLast(self):
        if self.size() > 0:
            return self._list.pop()
        return None

    def size(self):
        return len(self._list)
