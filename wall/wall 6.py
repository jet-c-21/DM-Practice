def f(n):
    if n == 1:
        return 1

    if n % 2 == 0:
        # even
        return f(n - 1) + 1
    else:
        # odd
        return f(n - 1) * 2


x = f(3)
print(x)
