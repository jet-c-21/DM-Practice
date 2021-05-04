def binary_expansion(n: int) -> list:
    res = list()

    while n != 0:
        res.insert(0, n % 2)
        n = n // 2

    return res


def modular_exponentiation(b: int, n: int, m: int):
    # n, m > 0
    power_bls = binary_expansion(n)
    print(power_bls)

    fact = list()
    po2 = 0
    for i in range(len(power_bls) - 1, -1, -1):
        d = power_bls[i]
        if d:
            print(2 ** po2)

        po2 += 1

    print(fact)

    # res = fact[0] % m
    # for i in range(1, len(fact)):
    #     res = res * (fact[i] % m)
    #
    # return res % m


def modular_exponentiation_from_pseudo(b: int, n: int, m: int):
    power_bls = binary_expansion(n)
    x = 1
    power = b % m

    for i in range(len(power_bls) - 1, -1, -1):
        if power_bls[i] == 1:
            x = (x * power) % m

        power = (power * power) % m

    return x


qq = modular_exponentiation_from_pseudo(3, 644, 645)
print(qq)
