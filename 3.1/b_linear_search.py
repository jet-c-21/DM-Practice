import random

seq = list(range(1, 21))
random.seed(777)
random.shuffle(seq)
print('The sequence:')
print(seq, '\n')


def linear_search(target: int, sequence: list):
    cost = 0
    for term in sequence:
        cost += 1
        if term == target:
            print('cost:', cost)
            return term


def linear_search_from_pseudo(target: int, sequence: list):
    cost = 0
    i = 0
    while i <= len(sequence) - 1 and target != sequence[i]:
        cost += 1
        i += 1

    if i <= len(sequence) - 1:
        location = i
    else:
        location = 0

    print('cost:', cost)
    return sequence[location]


linear_search(13, seq)
linear_search_from_pseudo(13, seq)
