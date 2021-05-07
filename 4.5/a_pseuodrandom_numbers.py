def linear_congruential(x: int, a=7, c=4, m=9):
    return (a * x + c) % m


def get_pseudorandom_num(x: int, count: int, a=7, c=4, m=9):
    result = list()
    for i in range(count):
        rand = x
        for _ in range(i):
            rand = linear_congruential(rand, a, c, m)
        result.append(rand)

    return result


def get_pseudorandom_num_from_ppt(x: int, count: int, a=7, c=4, m=9):
    result = [x]

    for i in range(count - 1):
        result.append(linear_congruential(result[-1], a, c, m))

    return result


qq = get_pseudorandom_num(3, 7)
print(qq)

qq = get_pseudorandom_num_from_ppt(3, 7)
print(qq)
