# coding: utf-8
"""
author: Jet Chien
GitHub: https://github.com/jet-chien
Create Date: 2021/5/4
"""


def slow_mod_exp(b: int, n: int, m: int):
    """
    (b^n) mod m = [(b^1)((b^n-1) mod m)] mod m

    :param b:
    :param n:
    :param m:
    :return: (b^n) mod m
    """

    r = b - (b // m) * m
    for i in range(2, n + 1):
        # iteration (2 ~ n) = n - 1
        p = b * r
        r = p - (p // m) * m

    return r


x = slow_mod_exp(3, 644, 645)
print(x)
