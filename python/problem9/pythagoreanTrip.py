#!/usr/bin/python

import math

def pythagorean():
    for m in reversed(xrange(2,1001)):
        for n in reversed(xrange(1,1000)):
            for k in xrange(1,101):
                a = k*(m**2 - n**2)
                b = k*(2*m*n)
                c = k*(m**2 + n**2)
                if a+b+c == 1000:
                    print a," ",b," ",c
                    return a*b*c
    

if __name__ == "__main__":
    print pythagorean()