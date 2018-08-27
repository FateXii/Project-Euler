#!/usr/bin/python

_file = open("numbers.txt","r")
nums = ''
for line in _file:
    nums += line.strip()
_file.close()

def greatestProduct(length = 4,series = nums):
    start = 0
    end = length
    largest = 0
    while end <= 1000:
        temp = 1
        numbers = series[start:end]
        for i in range(len(numbers)):
            temp *= int(numbers[i])
        if temp > largest:
            largest = temp
        start += 1
        end += 1
    return largest

if __name__ == "__main__":
    print greatestProduct(13)