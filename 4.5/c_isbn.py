def get_check_digit(code: str, m=11):
    s = 0
    for i in range(1, len(code) + 1):
        # print(f"{i} * {code[i - 1]}")
        s += i * int(code[i - 1])

    return s % m


def check_upc(product_code: str, m=11):
    s = 0
    for i in range(1, len(product_code) + 1):
        c = product_code[i - 1]
        if c.isnumeric():
            s += i * int(c)
        else:
            if c == 'X':
                s += i * 10

    if s % m == 0:
        return True
    else:
        return False


pc = '007288008'
print(get_check_digit(pc))

pc = '084930149X'
print(check_upc(pc))
#
# pc = '041331021641'
# print(check_upc(pc))
