import random

seq = list(range(1, 21))
random.seed(777)
random.shuffle(seq)
print('The sequence:')
print(seq, '\n')


def get_the_max_el(sequence: list):
    res = sequence[0]

    for i in range(1, len(sequence)):
        if res < sequence[i]:
            res = sequence[i]

    return res


x = get_the_max_el(seq)
print(x)
