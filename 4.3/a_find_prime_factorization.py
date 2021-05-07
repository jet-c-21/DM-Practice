import math

C = 0

def is_prime(n: int):
    global C
    if n == 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        C += 1
        if n % i == 0:
            return False

    return True


def find_prime_fact(n: int):
    global C
    result = list()

    i = 2
    while n != 1:
        C += 1
        if is_prime(i):
            if n % i == 0:
                result.append(i)
                n = n // i
                continue
        i += 1
    return result


x = find_prime_fact(641)
print(x)
print(C)
