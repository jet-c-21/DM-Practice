def get_check_digit(code: str, m=10):
    s = 0
    for i in range(1, len(code) + 1):
        if i % 2 != 0:
            s += 3 * int(code[i - 1])
        else:
            s += int(code[i - 1])

    for i in range(0, 10):
        if (s + i - 0) % 10 == 0:
            return i


def check_upc(product_code: str):
    s = 0
    for i in range(1, len(product_code) + 1):
        if i % 2 != 0:
            s += 3 * int(product_code[i - 1])
        else:
            s += int(product_code[i - 1])

    if s % 10 == 0:
        return True
    else:
        return False


pc = '79357343104'
print(get_check_digit(pc))

pc = '793573431042'
print(check_upc(pc))

pc = '041331021641'
print(check_upc(pc))
