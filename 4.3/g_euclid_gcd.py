def euclid_gcd_recursive(a: int, b: int):
    big = a
    small = b
    if b > a:
        big = b
        small = a

    r = big % small
    # print(f"big = {big}  small = {small}  r = {r}")
    if r == 0:
        return small
    else:
        return euclid_gcd_recursive(small, r)


def euclid_gcd_while(a: int, b: int):
    big = a
    small = b
    if b > a:
        big = b
        small = a

    r = big % small
    while r != 0:
        big = small
        small = r
        r = big % small

    return small


def euclid_gcd_no_alias(a: int, b: int):
    r = a % b
    if r == 0:
        return b
    else:
        return euclid_gcd_recursive(b, r)


def euclid_gcd_from_pseudo(a: int, b: int):
    x = a
    y = b
    while y != 0:
        r = x % y
        x = y
        y = r

    return x


def euclid_gcd_from_ppt(a: int, b: int):
    if b == 0:
        return a
    else:
        return euclid_gcd_from_ppt(b, a % b)


x = euclid_gcd_recursive(12921, 4234)
print(x)

x = euclid_gcd_recursive(4234, 12921)
print(x)

x = euclid_gcd_while(4234, 12921)
print(x)

x = euclid_gcd_no_alias(4234, 12921)
print(x)

x = euclid_gcd_from_pseudo(4234, 12921)
print(x)

x = euclid_gcd_from_ppt(4234, 12921)
print(x)

x = euclid_gcd_from_ppt(1111, 0)
print(x)