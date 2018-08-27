#!/usr/bin/python

import math


def listPrimes(n):
    """Returns a list of prime numbers <= n """
    primes = [2]
    for i in range(3, n + 1, 2):
        if is_prime(i):
            primes.append(i)   
    return primes




def prime(n):
    if n==1:
        return 2
    count = 1
    num = 3
    while(count <= n):
        if is_prime(num):
            count +=1
        num += 2
    return num

def is_prime(num):
    factor = 2
    if (num%factor == 0) and num != 2:
            return False
    factor = 3
    while (factor * factor <= num):
        if num%factor == 0:
            return False
        factor += 2
    return True
                   



if __name__ == "__main__":
    # print listPrimes(10001)
    # print listPrimes(20, 30)
    # print prime(100000)
    print is_prime(2)
    # n = 10001
    # primes = []
    # count = (n//1000)+(n%1000)
    # for i in range(n):
    #     primes += listPrimes(count*i, count*(i+1))
    #     if (len(primes) >= n):
    #         m = primes
    #         for i in m:
    #             print i
    #         break
    

