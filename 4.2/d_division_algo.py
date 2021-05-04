import pytest
import random


def division_algo(a: int, d: int):
    # b > 0
    q = a // d
    r = a - d * q

    return q, r


def division_algo_ppt(a: int, d: int):
    q = 0
    r = abs(a)
    while r >= d:
        r = r - d
        q = q + 1

    if a < 0:
        if r == 0:
            q = -q
        else:
            r = d - r
            q = -(q + 1)

    return q, r


def division_algo_while(a: int, d: int):
    q = 0
    r = abs(a)
    while r >= d:
        r = r - d
        q += 1

    if a < 0 and r > 0:
        r = d - r
        q = - (q + 1)

    return q, r


def division_algo_text_book(a: int, d: int):
    # has error when a is the multiple of d
    q = 0
    r = abs(a)
    while r >= d:
        r = r - d
        q += 1

    if a < 0 and r > 0:
        r = d - r
        q = - (q + 1)

    return q, r


def test_div_mod():
    tc = 90000
    lower_bound = 1
    upper_bound = 999999
    for i in range(tc):
        n1 = random.randint(lower_bound, upper_bound)
        n2 = random.randint(lower_bound, upper_bound)

        # res = int_add(n1, n2)
        res = division_algo(n1, n2)
        b_ls = division_algo_ppt(n1, n2)
        assert res == b_ls


x = division_algo(-11, 3)
print(x)

x = division_algo_ppt(-12, 3)
print(x)

x = division_algo_ppt(-11, 3)
print(x)
