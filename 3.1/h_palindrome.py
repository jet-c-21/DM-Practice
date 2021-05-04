import math


def palindrome_from_pseudo(s: str):
    res = True
    for f_idx in range(math.floor(len(s) / 2)):
        b_idx = len(s) - f_idx - 1
        if s[f_idx] != s[b_idx]:
            return False
    return res


x = palindrome_from_pseudo('fox')
print(x)
