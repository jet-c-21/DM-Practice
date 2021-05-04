def decimal_to_binary(n):
    res = list()
    b = 2
    while n != 0:
        r = n % b
        res.insert(0, r)
        n = n // b

    return res


def bin_arr_add(b_ls1: list, b_ls2: list):
    # fix len
    if len(b_ls1) != len(b_ls2):
        if len(b_ls2) > len(b_ls1):
            long_ls = b_ls2
            short_ls = b_ls1
        else:
            long_ls = b_ls1
            short_ls = b_ls2

        for _ in range(len(long_ls) - len(short_ls)):
            short_ls.insert(0, 0)

    res = list()
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


def int_add_from_pseudo_2(n1: int, n2: int):
    b_ls1 = decimal_to_binary(n1)
    b_ls2 = decimal_to_binary(n2)
    return bin_arr_add(b_ls1, b_ls2)


def int_mul(n1: int, n2: int):
    b_ls1 = decimal_to_binary(n1)
    b_ls2 = decimal_to_binary(n2)

    # alias
    if len(b_ls2) > len(b_ls1):
        long_ls = b_ls2
        short_ls = b_ls1
    else:
        long_ls = b_ls1
        short_ls = b_ls2

    temp = list()
    power_of_2 = 0
    for i in range(len(short_ls) - 1, -1, -1):
        d1 = short_ls[i]
        p = [0 for _ in range(power_of_2)]

        for j in range(len(long_ls) - 1, -1, -1):
            d2 = long_ls[j]
            p.insert(0, d1 * d2)

        temp.append(p)
        power_of_2 += 1

    res = temp[0]
    for i in range(1, len(temp)):
        added_b_ls = temp[i]
        res = bin_arr_add(res, added_b_ls)

    return res


def binary_expansion(n: int) -> list:
    res = list()

    while n != 0:
        res.insert(0, n % 2)
        n = n // 2

    return res


def int_mul_from_pseudo(a: int, b: int):
    a_bls = binary_expansion(a)
    b_bls = binary_expansion(b)

    # fix len
    if len(a_bls) != len(b_bls):
        if len(a_bls) > len(b_bls):
            long_ls = a_bls
            short_ls = b_bls
        else:
            long_ls = b_bls
            short_ls = a_bls

        for _ in range(len(long_ls) - len(short_ls)):
            short_ls.insert(0, 0)

    pp_ls = list()
    for j in range(len(a_bls)):
        idx = len(a_bls) - j - 1
        if b_bls[idx] == 1:
            p = a_bls + [0 for _ in range(j)]
        else:
            p = [0]

        pp_ls.append(p)

    res = [0]
    for i in range(len(pp_ls)):
        res = bin_arr_add(res, pp_ls[i])

    return res


# x = int_mul(6, 5)
x = int_mul_from_pseudo(6, 5)
print(x)
