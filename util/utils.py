#!/usr/bin/env python
from data.BinaryTree import ArrayBinaryTree
import math

def swap(list, i, j):
    t = list[i]
    list[i] = list[j]
    list[j] = t
