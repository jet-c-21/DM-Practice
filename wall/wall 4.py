import math


def get_first_prime_fact(n: int, start_prime=2):
    """
    return the first factor of n, otherwise n is a prime and return n
    :param start_prime: int
    :param n: int
    :return:
    """
    for i in range(start_prime, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            return i
    return n


def get_prime_fact_ls(n: int):
    result = list()
    if n in [1, 0]:
        return result

    first_fact = get_first_prime_fact(n)
    result.append(first_fact)

    while n != first_fact:
        n = n // first_fact
        first_fact = get_first_prime_fact(n, first_fact)
        result.append(first_fact)

    return result


def get_prime_fact_dict(prime_fact_ls: list):
    result = dict()
    for i in prime_fact_ls:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result


def prime_fact_gcd(a, b):
    if a * b == 0:
        return max(a, b)
    gcd = 1
    a_prime_fact_ls = get_prime_fact_ls(a)
    b_prime_fact_ls = get_prime_fact_ls(b)
    # print(a_prime_fact_ls)
    # print(b_prime_fact_ls)

    a_prime_fact_dict = get_prime_fact_dict(a_prime_fact_ls)
    b_prime_fact_dict = get_prime_fact_dict(b_prime_fact_ls)

    prime_union = set()
    prime_union.update(a_prime_fact_dict.keys())
    prime_union.update(b_prime_fact_dict.keys())

    for p in prime_union:
        prime_count_a = a_prime_fact_dict.get(p)
        if prime_count_a is None:
            prime_count_a = 0

        prime_count_b = b_prime_fact_dict.get(p)
        if prime_count_b is None:
            prime_count_b = 0

        prime_count_max = min(prime_count_a, prime_count_b)
        for _ in range(prime_count_max):
            gcd *= p

    return gcd


def prime_fact_lcm(a, b):
    if a * b == 0:
        # undefined
        return None

    gcd = 1
    a_prime_fact_ls = get_prime_fact_ls(a)
    b_prime_fact_ls = get_prime_fact_ls(b)

    a_prime_fact_dict = get_prime_fact_dict(a_prime_fact_ls)
    b_prime_fact_dict = get_prime_fact_dict(b_prime_fact_ls)

    prime_union = set()
    prime_union.update(a_prime_fact_dict.keys())
    prime_union.update(b_prime_fact_dict.keys())

    for p in prime_union:
        prime_count_a = a_prime_fact_dict.get(p)
        if prime_count_a is None:
            prime_count_a = 0

        prime_count_b = b_prime_fact_dict.get(p)
        if prime_count_b is None:
            prime_count_b = 0

        prime_count_max = max(prime_count_a, prime_count_b)
        for _ in range(prime_count_max):
            gcd *= p

    return gcd


def find_prime_fact_dict(n: int):
    prime_fact_ls = get_prime_fact_ls(n)
    return get_prime_fact_dict(prime_fact_ls)


x = find_prime_fact_dict(92928)
print(x)

x = find_prime_fact_dict(123552)
print(x)

print(2 ** 8 * 3 ** 3 * 11 ** 2 * 13 ** 1)
