#!/usr/bin/python

if __name__ == "__main__":
    total = 0
    for i in range(1000):
        if ((not(i%3)) or (not(i%5))):
            total += i
    print(total)    