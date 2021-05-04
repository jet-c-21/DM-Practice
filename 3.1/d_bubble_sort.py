seq = [5, 2, 4, 1, 3]
print('seq before sort:', seq)


def bubble_sort(sequence: list):
    for i in range(len(sequence) - 1, -1, -1):
        for j in range(i):
            curr_term = sequence[j]
            next_term = sequence[j + 1]

            if curr_term > next_term:
                sequence[j] = next_term
                sequence[j + 1] = curr_term

            # print(j, end=', ')
        # print()

    return sequence


def bubble_sort_from_pseudo(sequence: list):
    for i in range(0, len(sequence) - 1):
        for j in range(0, len(sequence) - 1 - i):
            if sequence[j] > sequence[j + 1]:
                sequence[j], sequence[j + 1] = sequence[j + 1], sequence[j]
            # print(j, end=', ')
        # print()
    return sequence


x = bubble_sort_from_pseudo(seq)
print(x)

x = bubble_sort(seq)
print(x)
print(seq)
