#!/usr/bin/python3
"""minimum operations"""
from math import sqrt


def minOperations(n):

    if n <= 1:
        return 0
    elif is_n_prime(n):
        return n
    else:
        prime = small_prime(n)
        if prime:
            return prime + minOperations(int(n/prime))


def is_n_prime(n):

    result = True
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            result = False
    return result


def small_prime(n):

    result = None
    for i in range(2, int(n/2 + 1)):
        if n % i == 0:
            result = i
            break
    return result
