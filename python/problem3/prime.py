#!/usr/bin/python
import math

def findLargestPrime(n):
    largestPrime = 0
    while not(n%2):
        largestPrime = 2
        n //= 2
    
    for i in range(3, int(math.sqrt(n)),2):
        if not(n%i):
            largestPrime = i
            n //= i

    if (n > 2):
        largestPrime = n
    return largestPrime

if __name__ == "__main__":
    print findLargestPrime(13195)
    #print findLargestPrime(600851475143)