import math
import time
from typing import Callable


def is_prime_slow(n: int):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def is_prime(n: int):
    if n < 2:
        return False

    if n == 2:
        return True

    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def find_prime_in_time(method: Callable, sec=60):
    result = list()
    start = time.time()
    i = 2
    while time.time() - start < sec:
        if method(i):
            result.append(i)
        i += 1

    print(f"method: {method.__name__}() find {len(result)} of prime, the biggest founded prime is {result[-1]}")


find_prime_in_time(is_prime_slow, 10)
find_prime_in_time(is_prime, 10)
