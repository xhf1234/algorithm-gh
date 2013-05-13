#!/usr/bin/env python

def comb(tList, k, cbk):
    n = len(tList)
    if k>n:
        print 'illegal k=%d while n=%d' %(k,n)
    if n is 0 or k is 0:
        return
    c = [i for i in range(k)]
    def visit():
        dList = [tList[i] for i in c]
        cbk(dList)
    while True:
        visit()
        i = -1
        for i in range(k-1):
            if c[i] != c[i+1]-1:
                break
        else:
            i = i+1
            if c[i] == n-1:
                break
        c[i] = c[i]+1
        for j in range(i):
            c[j] = j

def comb_recursive(tList, tStart, k, rList, rStart, cbk):
    n = len(tList)-tStart
    if k>n:
        print 'illegal k=%d while n=%d' %(k,n)
        return
    if k == n or k == 0:
        for i in range(k):
            rList[rStart+i] = tList[tStart+i]
        cbk(rList)
        return
    #choose tList[tStart]
    rList[rStart] = tList[tStart]
    comb_recursive(tList, tStart+1, k-1, rList, rStart+1, cbk)
    #skip tList[tStart]
    comb_recursive(tList, tStart+1, k, rList, rStart, cbk)

def main():
    def cbk(tList):
        print tList
    tList = ['a', 'b', 'c', 'd', 'e']
    rList = [None]*2
    comb_recursive(tList, 0, 2, rList, 0, cbk)

if __name__ == '__main__':
    main()
