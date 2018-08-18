#!/usr/bin/python

def findLargestPaliProd(_x = 1000,_y = 1000):
    largest = 0
    for x in reversed(range(100,_x)):
        for y in reversed(range(100,_y)):
            result = x*y
            if(str(result)==str(result)[::-1]):
                if (result > largest):
                    largest = result
    return largest

print findLargestPaliProd()

    