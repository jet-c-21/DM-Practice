import math

C = 0  # Cost


def get_first_prime_fact(n: int, start_prime=2):
    """
    return the first factor of n, otherwise n is a prime and return n
    :param start_prime: int
    :param n: int
    :return:
    """
    global C

    for i in range(start_prime, math.ceil(math.sqrt(n)) + 1):
        C += 1
        if n % i == 0:
            return i
    return n


def get_prime_fact(n: int):
    global C
    result = list()
    if n == 1:
        return result

    first_fact = get_first_prime_fact(n)
    result.append(first_fact)

    while n != first_fact:
        C += 1
        n = n // first_fact
        first_fact = get_first_prime_fact(n, first_fact)
        result.append(first_fact)

    return result


print(get_prime_fact(100), f"C = {C}")
C = 0

print(get_prime_fact(641), f"C = {C}")
C = 0

print(get_prime_fact(999), f"C = {C}")
C = 0

print(get_prime_fact(1024), f"C = {C}")
C = 0

print(get_prime_fact(7007), f"C = {C}")
C = 0

print(get_prime_fact(2), f"C = {C}")
C = 0

print(get_prime_fact(1), f"C = {C}")
C = 0

print(get_prime_fact(143), f"C = {C}")
C = 0
