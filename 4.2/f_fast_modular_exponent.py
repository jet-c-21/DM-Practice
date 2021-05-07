def binary_expansion(n: int) -> list:
    res = list()

    while n != 0:
        res.insert(0, n % 2)
        n = n // 2

    return res


def modular_exponentiation_from_pseudo(b: int, n: int, m: int):
    power_bls = binary_expansion(n)
    x = 1
    power = b % m

    for i in range(len(power_bls) - 1, -1, -1):
        if power_bls[i] == 1:
            x = (x * power) % m

        power = (power * power) % m

    return x


def modular_exponentiation_from_pseudo_verbose(b: int, n: int, m: int):
    power_bls = binary_expansion(n)
    x = 1
    power = b % m
    print(f"init => x = {x}, power = {power} \n")
    for i in range(len(power_bls) - 1, -1, -1):
        i_str = str(i).ljust(2)
        bin_str = str(power_bls[i])

        if power_bls[i] == 1:
            x_str = f"({x} * {power}) mod {m} = {(x * power) % m}".ljust(25)
            x = (x * power) % m
        else:
            x_str = str(x).ljust(25)

        power_str = f"({power} * {power}) mod {m} = {(power * power) % m}"
        power = (power * power) % m

        print(f"i = {i_str}, bin = {bin_str}, x = {x_str}(x = {str(x).ljust(3)}), power = {power_str}")

    return x


qq = modular_exponentiation_from_pseudo_verbose(7, 644, 645)
print(qq)

# qq = modular_exponentiation_from_pseudo_verbose(3, 2003, 99)
# print(qq)
