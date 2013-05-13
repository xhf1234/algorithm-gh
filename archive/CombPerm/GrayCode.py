#!/usr/bin/env python

def G(k):
    """
        the kth gray code in binary
    """
    return k^(k>>1)

def gray_code(d, cbk):
    """
        iterate the d bits gray code
    """
    n = 2**d
    for i in range(0, n):
        cbk(G(i))

def main():
    d = 3
    def cbk(k):
        n = 2**d
        print bin(n+k)[3:]
    gray_code(d, cbk)

    tList = ['a', 'b', 'c']
    def cbk(k):
        dList = []
        for i in range(len(tList)):
            if k&(1<<(len(tList)-i-1)):
                dList.append(tList[i])
        print dList
    gray_code(len(tList), cbk)



if __name__ == '__main__':
    main()
