#!/bin/python3
# encoding: utf-8

import sys

# sys.setrecursionlimit(100000)

from random import randint


# 辗转相除法
def eucelidean_algo(a, b):
    if a < b:
        a, b = b, a
    c = a % b
    if c == 0:
        return b
    else:
        return eucelidean_algo(c, b)

# 更减相损术
def gcd(a, b):
    if a == b:
        return b
    if a < b:
        a, b = b, a
    return gcd(a - b, b)

# 结合以上两种算法
def combined_algo(a, b):
    is_even_a = a % 2 == 0
    is_even_b = b % 2 == 0
    if is_even_a and is_even_b:
        return combined_algo(a / 2., b / 2.) * 2
    elif is_even_a and (not is_even_b):
        return combined_algo(a / 2., b)
    elif (not is_even_a) and is_even_b:
        return combined_algo(a, b / 2.)
    else:
        if a == b:
            return b
        if a < b:
            a, b = b, a
        return combined_algo(a - b, b)

if __name__ == '__main__':
    functions = [eucelidean_algo, gcd, combined_algo]
    for i in range(4):
        print("=" * 16)
        nums = tuple(randint(10**3, 10**7) for i in range(2))
        for func in functions:
            print("{}({}) => {}".format(func.__name__, nums, func(*nums)))

