import string


def caesar_cypher_encrypt(s: str, k=3):
    res = ''
    upper_letter = string.ascii_uppercase
    for c in s:
        if c != ' ':
            idx = (upper_letter.index(c) + k) % len(upper_letter)
            res += upper_letter[idx]
        else:
            res += ' '

    return res


def caesar_cypher_decrypt(s: str, k=3):
    res = ''
    upper_letter = string.ascii_uppercase
    for c in s:
        if c != ' ':
            idx = (upper_letter.index(c) - k) % len(upper_letter)
            res += upper_letter[idx]
        else:
            res += ' '

    return res


def get_shift_idx(x, a=7, c=3, m=26):
    return (a * x + c) % m


def print_encrypt_map():
    upper_letter = string.ascii_uppercase
    for i in range(len(upper_letter)):
        h = get_shift_idx(i)
        print(f"{upper_letter[i]} => {upper_letter[h]}")


print_encrypt_map()

# x = caesar_cypher_encrypt('MEET YOU IN THE PARK')
# print(x)
#
# x = caesar_cypher_decrypt('STOP GLOBAL WARNING', 11)
# print(x)
#
# x = caesar_cypher_decrypt('LEWLYPLUJL PZ H NYLHA ALHJOLY', 7)
# print(x)
