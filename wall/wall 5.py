def fib(n):

    if n == 0:
        return 0

    if n == 1 or n == 2:
        return 1

    return fib(n - 1) + fib(n - 2)


for i in range(1, 7):
    print(fib(i))
