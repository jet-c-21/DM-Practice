SEQ = [8, 4, 6, 9, 2, 3, 1]


def selection_sort(sequence: list):
    # it is literally as same as the pseudo code
    for i in range(len(sequence) - 1):
        smallest_term_idx = i

        for j in range(i + 1, len(sequence)):
            if sequence[j] < sequence[smallest_term_idx]:
                smallest_term_idx = j

        sequence[i], sequence[smallest_term_idx] = sequence[smallest_term_idx], sequence[i]

    return sequence


def selection_sort_reverse(sequence: list):
    for i in range(len(sequence) - 1):
        largest_term_idx = i
        for j in range(i + 1, len(sequence)):
            if sequence[j] > sequence[largest_term_idx]:
                largest_term_idx = j

        sequence[i], sequence[largest_term_idx] = sequence[largest_term_idx], sequence[i]

    return sequence


# x = selection_sort(SEQ)
# print(x)

x = selection_sort_reverse(SEQ)
print(x)
