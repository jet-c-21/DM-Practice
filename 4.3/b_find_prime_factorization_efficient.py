import math

C = 0


def get_first_prime_fact(n: int):
    """
    return the first factor of n, otherwise n is a prime and return n
    :param n: int
    :return:
    """
    global C

    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        C += 1
        if n % i == 0:
            return i
    return n


def get_prime_fact(n: int):
    global C
    result = list()

    first_fact = get_first_prime_fact(n)
    result.append(first_fact)

    while n != first_fact:
        C += 1
        n = n // first_fact
        first_fact = get_first_prime_fact(n)
        result.append(first_fact)

    return result


x = get_prime_fact(7007)
print(x)
print(C)
