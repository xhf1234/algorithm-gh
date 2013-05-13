#!/usr/bin/env python
import math

class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
    
class BinaryTree(object):
    def insert(self, value):
        pass
    def size(self):
        pass

class ArrayBinaryTree(BinaryTree):
    def __init__(self, list=None):
        if list is None:
            self._list = []
        else:
            self._list = list
    
    def insert(self, value):
        self._list.append(value)

    def __len__(self):
        return len(self._list)

    def size(self):
        return len(self)

    def value(self, index):
        """ return the array value in given index, or None if it's a invalid index"""
        if (index<0 or index >= self.size()):
            return None
        return self._list[index]
        
    def left(self, parentIndex):
        """return the left child's value of the given parentIndex, or None if left child not exists"""
        left = 2*parentIndex+1;
        return self.value(left)
        
    def right(self, parentIndex):
        """return the right child's value of the given parentIndex, or None if right child not exists"""
        right = 2*parentIndex+2;
        return self.value(right)
    
    def set(self, index, value):
        if index >= self.size():
            return
        self._list[index] = value

    def height(self):
        return int(math.log(len(self)+1, 2))
