import random
import math

seq = [1, 2, 3, 5, 6, 7, 8, 10, 12, 13, 15, 16, 18, 19, 20, 22]


def binary_search(target: int, sequence: list):
    cost = 0
    s = sequence
    flag = True
    while flag:
        cost += 1
        mid_idx = len(s) // 2
        less_ls = s[0:mid_idx]
        most_ls = s[mid_idx:len(s)]

        if less_ls[-1] == target:
            print('cost:', cost)
            return less_ls[-1]

        if most_ls[-1] == target:
            print('cost:', cost)
            return most_ls[-1]

        if target > less_ls[-1]:
            s = most_ls
        else:
            s = less_ls


def binary_search_from_pseudo(target: int, sequence: list):
    cost = 0

    i = 1
    j = len(sequence) - 1
    while i < j:
        cost += 1

        m = math.floor((i + j) / 2)
        curr_term = sequence[m]
        if target > curr_term:
            i = m + 1
        else:
            j = m

    if target == sequence[i]:
        location = i
    else:
        location = 0

    print('cost:', cost)
    return sequence[location]


x = binary_search(19, seq)
print(x)

x = binary_search_from_pseudo(19, seq)
print(x)


