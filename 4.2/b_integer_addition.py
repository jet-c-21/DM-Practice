import pytest
import random


def decimal_to_binary(n):
    res = list()
    b = 2
    while n != 0:
        r = n % b
        res.insert(0, r)
        n = n // b

    return res


def int_add(n1: int, n2: int):
    res = list()
    b_ls1 = decimal_to_binary(n1)
    b_ls2 = decimal_to_binary(n2)

    if len(b_ls1) != len(b_ls2):
        if len(b_ls2) > len(b_ls1):
            long_ls = b_ls2
            short_ls = b_ls1
        else:
            long_ls = b_ls1
            short_ls = b_ls2

        for _ in range(len(long_ls) - len(short_ls)):
            short_ls.insert(0, 0)

    i = 0
    c = 0
    while i <= len(b_ls1):
        idx = len(b_ls1) - i - 1
        if idx == -1:
            if c != 0:
                res.insert(0, c)
            break

        d1 = b_ls1[idx]
        d2 = b_ls2[idx]

        s = d1 + d2 + c
        r = s % 2
        print(f"s = {s}  r = {r}")
        res.insert(0, r)
        c = s // 2

        i += 1

    return res


def int_add_from_pseudo(n1: int, n2: int):
    res = list()
    b_ls1 = decimal_to_binary(n1)
    b_ls2 = decimal_to_binary(n2)

    if len(b_ls1) != len(b_ls2):
        if len(b_ls2) > len(b_ls1):
            long_ls = b_ls2
            short_ls = b_ls1
        else:
            long_ls = b_ls1
            short_ls = b_ls2

        for _ in range(len(long_ls) - len(short_ls)):
            short_ls.insert(0, 0)

    c = 0
    for i in range(len(b_ls1)):
        idx = len(b_ls1) - i - 1
        q = (b_ls1[idx] + b_ls2[idx] + c) // 2
        r = b_ls1[idx] + b_ls2[idx] + c - 2 * q
        res.insert(0, r)
        c = q

    res.insert(0, c)

    return res


def int_add_from_pseudo_2(n1: int, n2: int):
    res = list()
    b_ls1 = decimal_to_binary(n1)
    b_ls2 = decimal_to_binary(n2)

    if len(b_ls1) != len(b_ls2):
        if len(b_ls2) > len(b_ls1):
            long_ls = b_ls2
            short_ls = b_ls1
        else:
            long_ls = b_ls1
            short_ls = b_ls2

        for _ in range(len(long_ls) - len(short_ls)):
            short_ls.insert(0, 0)

    c = 0
    for i in range(len(b_ls1)):
        idx = len(b_ls1) - i - 1
        d1, d2 = b_ls1[idx], b_ls2[idx]
        s = d1 + d2 + c
        q = s // 2
        r = s - 2 * q
        res.insert(0, r)
        c = q

    if c != 0:
        res.insert(0, c)

    return res


def test_int_add():
    tc = 90000
    lower_bound = 1
    upper_bound = 999999
    for i in range(tc):
        n1 = random.randint(lower_bound, upper_bound)
        n2 = random.randint(lower_bound, upper_bound)

        # res = int_add(n1, n2)
        res = int_add_from_pseudo_2(n1, n2)
        b_ls = decimal_to_binary(n1 + n2)
        assert res == b_ls


def int_add_from_str(n1: str, n2: str):
    result = ''
    max_len = max(len(n1), len(n2))
    n1 = n1.zfill(max_len)
    n2 = n2.zfill(max_len)

    b_map = {'1': 1, '0': 0}
    carry = 0
    print(max_len)
    for i in range(max_len - 1, -1, -1):
        d1, d2 = b_map[n1[i]], b_map[n2[i]]
        s = d1 + d2 + carry
        q = s // 2
        r = s - q * 2
        result = str(r) + result

        carry = q

    if carry != 0:
        result = '1' + result

    return result


# test_int_add()
# x = int_add_from_pseudo(15, 17)
x = int_add_from_pseudo_2(6, 24)
print(x)

x = int_add_from_str('110', '11000')
print(x)
