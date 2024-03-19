#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """Minimum Operations"""
    if n <= 1:
        return 0
    for i in range(2, n):
        if n % i == 0:
            return i + minOperations(n // i)
    return n
