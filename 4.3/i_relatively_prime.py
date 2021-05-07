def gcd(a: int, b: int):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def is_rel_prime(sequence: list):
    for i in range(1, len(sequence)):
        for j in range(0, i):
            if gcd(sequence[i], sequence[j]) != 1:
                return False
            # print(f"{j}, ", end='')
        # print()
    return True


# is_rel_prime([1, 2, 3])
# print()

print(is_rel_prime([1, 2, 6]))
