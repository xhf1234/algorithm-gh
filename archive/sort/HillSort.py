#!/usr/bin/env python
from util.utils import randomList

def hill_sort(list_):
    if not list_:
        return
    size = len(list_)
    step = int(round(size/2))
    while step > 0:
        inverse_step = 0-step
        for start in range(step):
            for i in range(start+step, size, step):
                temp = list_[i]
                for j in range(i-step, -1, inverse_step):
                    if list_[j] > temp:
                        list_[j+step] = list_[j] 
                    else:
                        list_[j+step] = temp
                        break
                else:
                    list_[start] = temp
        step = int(round(step/2.2))

def main():
    tList = randomList(100)
    hill_sort(tList)
    print tList

if __name__ == '__main__':
    main()
