#!/usr/bin/python

import math

#Checks if _x is divisible by all numbers from 1 to _y
#
# def isDivisible(_x = 2520,_y = 10):  
#     rem = 0
#     for y in range(1,(_y + 1)):
#         rem += _x%y
#         if (rem):
#             return False
#     if not(rem):
#         return True


# def findSmallestMultiple(_y = 25):
#     for i in range(2520,999999999,2):
#         if(isDivisible(i,_y)):
#             return i
#     return -1

def listPrimes(n = 10):
    """Returns a list of prime number from 2 to n"""
    prime = [2]
    prime += range(3, n+1, 2)
    for i in range(3,int(math.sqrt(n))+1):
        sieve = range(i**2, n+1, i)
        if (set(sieve).isdisjoint(set(prime))):
            continue
        for j in sieve:
            if prime.count(j):
                prime.remove(j)   
    return prime

def findPrimeFactor(_number = 20):
    """Find prime factors or a number returns dictionary in format
        {prime:index, prime:index, ...} for 10 result is {2:1,5:1} meaning
        10 = 2^1*5*1 """
    primes = listPrimes(_number)
    primeFactors = {}
    for i in primes:
        count = 0
        while not(_number % i):
            count += 1
            primeFactors[i] = count
            _number //= i

    return primeFactors

def findPrimeFactorRange(_number = 20):
    """Find prime factors for a ranges of numbers"""
    primeFactors = {}
    for x in range(2,_number + 1):
        primeFactors[x] = findPrimeFactor(x)
    return primeFactors

def cleanEmptyDicValues(_dictionary):
    for key in _dictionary.copy():
        if not(_dictionary[key]):
            del(_dictionary[key])

def mcpf(_number = 20):
    """List most common prime factors"""
    f = findPrimeFactorRange(_number)
    mostCommonPrime = {}
    for i in range(_number + 1):
        mostCommonPrime[i] = 0
    for i in f:
        for j in f[i]:
            if mostCommonPrime[j] < f[i][j]:
                mostCommonPrime[j] = f[i][j] 
    cleanEmptyDicValues(mostCommonPrime)
    return mostCommonPrime

def lcm(_number = 20):
    """Returns lowest common multiple for a range 1 to _number"""
    mostCommonPrime = mcpf(_number)
    result = 1
    for key in mostCommonPrime:
        result *= key ** mostCommonPrime[key]
    return result



if __name__ == "__main__":
    
    print listPrimes(10001)