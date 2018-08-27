#!/usr/bin/python

def fib(x):
    if (x <= 0):
        return 1
    return fib(x-1) + fib(x-2)




if __name__ == "__main__":
    count = 0
    total = 0
    while (fib(count) < 4000000):
        if not(fib(count)%2):
            total += fib(count)
        count += 1
    print total