#!/usr/bin/env python
"""Implements math functions without using operators except for '+' and '-' """

__author__ = "SmileySlays"


def add(x, y):
    """Add two integers. Handles negative values."""
    return x + y


def multiply(x, y):
    """Multiply x with y. Handles negative values of x or y."""
    total = 0
    if y < 0:
        for num in range(y, 0):
            total = add(total, -x)
        return total
    elif y > 0:
        for num in range(y):
            total = add(total, x)
        return total
    else:
        return 0


def power(x, n):
    """Raise x to power n, where n >= 0"""
    total = x
    if n > 1:
        for num in range(n-1):
            total = multiply(total, x)
        return total
    elif n == 1:
        return x
    else:
        return 0


def factorial(x):
    """Compute factorial of x, where x > 0"""
    total = 1
    if x > 0:
        for num in range(x, 0, -1):
            total = multiply(total, num)
        return total
    else:
        return 1


def fibonacci(n):
    """Compute the nth term of fibonacci sequence"""
    fibo_list = [0]
    for num in range(n):
        if num == 0 or num == 1:
            fibo_list.append(num)
        else:
            fibo_list.append(add(fibo_list[num], fibo_list[num-1]))
    return fibo_list[-1]


if __name__ == '__main__':
    print("Add:", add(2, 4))
    print("Multiply:", multiply(6, -8))
    print("Power:", power(2, 8))
    print("Factorial:", factorial(4))
    print("Fibonacci:", fibonacci(8))
