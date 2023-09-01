#!/bin/python3
def is_prime(num):
    if not (isinstance(num, int) and num > 1):
        return False
    if num == 2 or num == 3:
        return True
    if not (num > 3 and (num-1)%6 == 0 or (num+1)%6 == 0):
        return False
    limit = int(num ** 0.5) + 1
    for number in range(2, limit):
        if num % number == 0:
            return False
    return True
