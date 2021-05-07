def get_divisor_ls(n: int):
    result = list()
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result


def easy_gcd(a: int, b: int):
    a_div_ls = get_divisor_ls(a)
    b_div_ls = get_divisor_ls(b)

    # alias
    long_div_ls = a_div_ls
    short_div_ls = b_div_ls
    if b_div_ls > a_div_ls:
        long_div_ls = b_div_ls
        short_div_ls = a_div_ls

    gcd = 1
    for i in range(1, len(short_div_ls)):
        d = short_div_ls[i]
        if d in long_div_ls and d > gcd:
            gcd = d

    return gcd


x = easy_gcd(24, 36)
print(x)

x = easy_gcd(48, 24)
print(x)

x = easy_gcd(17, 22)
print(x)

x = easy_gcd(168, 36)
print(x)
