def base_b_expansion(n: int, b: int) -> str:
    # b > 1
    res = list()

    while n // b != 0:
        q = n // b
        r = n % b
        print(f"q = {q}  r = {r}")
        res.insert(0, r)

        n = q

    res.insert(0, n % b)

    s = ''
    for d in res:
        s += str(d)

    print(f"res = {res}")

    return s


def base_b_expansion_from_pseudo(n: int, b: int) -> list:
    res = []
    q = n
    k = 0
    while q != 0:
        res.insert(len(res) - k, q % b)
        q = q // b
        k += 1

    return res


def base_b_expansion_from_pseudo_2(n: int, b: int) -> list:
    res = list()
    q = n

    while q != 0:
        res.insert(0, q % b)
        q = q // b

    return res


def base_b_expansion_from_pseudo_3(n: int, b: int) -> list:
    res = list()

    while n != 0:
        res.insert(0, n % b)
        n = n // b

    return res


x = base_b_expansion_from_pseudo_3(177130, 16)
x = base_b_expansion_from_pseudo_3(177130, 2)
print(x)
