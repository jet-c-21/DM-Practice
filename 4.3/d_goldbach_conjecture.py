import pytest
import math
from tqdm import tqdm


def is_prime(n: int):
    if n == 2:
        return True
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def goldbach_conjecture(n: int):
    # 44 = 3 + 41
    if n <= 2:
        print(f"{n} is less than 2!")
        return

    if n % 2 != 0:
        print(f"{n} is not an even integer!")
        return

    # end = math.ceil(math.sqrt(n)) + 2
    end = n + 1
    for i in range(2, end):
        if is_prime(i):
            j = n - i
            if is_prime(j):
                return i, j

def test_goldbach():
    E = 2147483646
    for x in tqdm(range(4, E + 1, 2)):
        res = goldbach_conjecture(x)
        if not isinstance(res, tuple):
            print('Exception:', x)
            break
        else:
            # print(f"{str(x).ljust(len(str(E)))} => {res}")
            pass
    print('done!')


if __name__ == '__main__':
    test_goldbach()
    # x = goldbach_conjecture(12)
    # print(x)