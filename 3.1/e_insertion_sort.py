seq = [5, 2, 4, 1, 3]


# seq = [5, 2, 4, 1, 3]

def insertion_sort(sequence: list):
    for i in range(1, len(sequence)):
        j = 0
        while j < i:
            if sequence[i] < sequence[j]:
                term = sequence.pop(i)
                sequence.insert(j, term)

            j += 1

    return sequence


def insertion_sort_from_pseudo(sequence: list):
    for j in range(1, len(sequence)):
        i = 0
        while sequence[j] > sequence[i]:
            i += 1

        temp = sequence[j]
        # print(f"j = {j}  i = {i}")

        for k in range(j - i):
            sequence[j - k] = sequence[j - k -1]
        sequence[i] = temp

    return sequence


x = insertion_sort(seq)
print(x)

x = insertion_sort_from_pseudo(seq)
# print(x)
