#! /usr/bin/python

def isPrime(i = 5):
    factor = 2
    if (not(i%factor) and (i != factor)):
        return False
    factor = 3
    while factor**2 <= i:
        if not(i%factor):
            return False
        factor += 2
    return True


if __name__ ==  "__main__":
    sum_ = 0
    for i in xrange(2,2000000):
        if isPrime(i):
           # print i
            sum_ += i
    print sum_
