#!/usr/bin/env python

def enum(dList, cbk):
    if dList is None or len(dList) is 0:
        return
    tList = [None]*len(dList)
    a = [0]*len(dList)
    m = [len(subList) for subList in dList] #a[i]<m[i]
    running = True
    while running:
        for i in range(0, len(dList)):
            tList[i] = dList[i][a[i]]
        cbk(tList)
        for i in range(len(dList)-1, -1, -1):
            if a[i]<m[i]-1:
                a[i] = a[i]+1
                break
            elif i>0:
                a[i] = 0
            else:
                running = False
                break

def main():
    def cbk(tList):
        print tList
    dList = [
        ['a', 'b', 'c'],
        ['d', 'e'],
        ['f', 'g', 'h']
    ]
    enum(dList, cbk)

if __name__ == '__main__':
    main()
