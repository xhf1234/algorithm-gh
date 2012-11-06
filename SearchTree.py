#!/usr/bin/env python
from data.Queue import Queue

class _Node(object):
    def __init__(self, value):
        self.value = value
        self.parent, self.left, self.right = None, None, None

    def __str__(self):
        return str(self.value)
    
class SearchTree(object):
    def __init__(self, values):
        self.root = None
        for value in values:
            self.insert(value)

    def insert(self, value):
        c = _Node(value)
        if self.root is None:
            self.root = c
        else:
            p = self.root
            while True:
                if value <= p.value:
                    if p.left is None:
                        p.left = c
                        c.parent = p
                        break
                    else:
                        p = p.left
                        continue
                else:
                    if p.right is None:
                        p.right = c
                        c.parent = p
                        break
                    else:
                        p = p.right
                        continue

    def search(self, value):
        r = [None];
        def visit(node):
            if node.value == value:
                r[0] = node
                return True
            return False
        self.__walk(self.root, visit)
        return r[0]

    def __minimum(self, node):
        p = node
        if p is None:
            return None
        while p.left is not None:
            p = p.left
        return p

    def minimum(self):
        minNode = self.__minimum(self.root)
        return self.__nodeValue(minNode)

    def __maximum(self, node):
        p = node
        if p is None:
            return None
        while p.right is not None:
            p = p.right
        return p

    def maximum(self):
        maxNode = self.__maximum(self.root)
        return self.__nodeValue(maxNode)

    def walk(self):
        """ walk and return the value list"""
        rList = []
        def visit(node):
            rList.append(node.value)
            return False
        self.__walk(self.root, visit)
        return rList

    def __walk(self, node, visit):
        """
        param node, start walking with this node
        param visit, callback, visit the current node, return True if need to stop walking
        """
        if node is None:
            return
        self.__walk(node.left, visit)
        if visit(node):
            return
        self.__walk(node.right, visit)

    def __successor(self, node):
        if node is None:
            return None
        if node.right is not None:
            return self.__minimum(node.right)
        p = node.parent
        while p is not None and p.right is node:
            node = p
            p = p.parent
        return p

    def successor(self, value):
        node = self.search(value)
        node = self.__successor(node)
        return self.__nodeValue(node)

    def __predecessor(self, node):
        if node is None:
            return None
        if node.left is not None:
            return self.__maximum(node.left)
        p = node.parent
        while p is not None and p.left is node:
            node = p
            p = p.parent
        return p

    def predecessor(self, value):
        node = self.search(value)
        node = self.__predecessor(node)
        return self.__nodeValue(node)
    
    def __nodeValue(self, node):
        if node is None:
            return None
        return node.value

    def __replace(self, src, dst):
        """ replace src as dst """
        if src.parent is None:
            self.root = dst
        elif src.parent is not dst:
            if src.parent.left is src:
                src.parent.left = dst
            else:
                src.parent.right = dst
        if src.left is not None and src.left is not dst:
            src.left.parent = dst
        if src.right is not None and src.right is not dst:
            src.right.parent = dst
        if src.parent is not dst:
            dst.parent = src.parent
        if src.left is not None and src.left is not dst:
            dst.left = src.left
        if src.right is not None and src.right is not dst:
            dst.right = src.right

        src.left, src.right, src.parent = None, None, None

    def delete(self, value):
        todel = self.search(value)
        if todel is None:
            return
        if todel.left is None and todel.right is None:
            if todel.parent is None:
                self.root = None
                return
            else:
                if todel.parent.left is todel:
                    todel.parent.left = None
                else:
                    todel.parent.right = None
                return
        if todel.left is not None and todel.right is not None:
            sucNode = self.__successor(todel)
            if sucNode.right is not None:
                self.__replace(sucNode, sucNode.right)
            self.__replace(todel, sucNode)
            return
        if todel.left is not None:
            self.__replace(todel, todel.left)
        else:
            self.__replace(todel, todel.right)

    def __str__(self):
        if self.root is None:
            return "empty tree"
        space = {} 
        queue = Queue()
        min = 0
        tList = []
        ENTER = 1
        lastNode = False
        
        space[self.root.value] = 0
        queue.enqueue(ENTER) #next one is the last node in the current tree level
        queue.enqueue(self.root)

        while queue.size() > 0:
            node = queue.dequeue()
            if node is ENTER:
                lastNode = True
                continue
            tList.append(node)
            if lastNode:
                tList.append(ENTER)
            if node.left is not None:
                value = space[node.value] - 1
                space[node.left.value] = value
                if value < min:
                    min = value
                queue.enqueue(node.left)
            if node.right is not None:
                space[node.right.value] = space[node.value] + 1
                queue.enqueue(node.right)
            if lastNode and queue.size() > 0:
                tNode = queue.popLast()
                queue.enqueue(ENTER)
                queue.enqueue(tNode)
                lastNode = False

        result = ""
        cursor = 0
        for node in tList:
            if node is ENTER:
                result += '\n'
                cursor = 0
            else:
                result = result + ' '*(space[node.value]-min-cursor) + str(node.value)
                cursor = space[node.value]-min+1
        return result

if __name__ == '__main__':
    values = [3, 4, 5, 7, 2, 0, 9, 1, 8, 6]
    tree = SearchTree(values)
    print tree.walk()
    for v in range(0, 10):
        tree.delete(v)
        print tree.walk()
