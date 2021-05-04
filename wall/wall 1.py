import numpy as np

k_ls = np.array([0])
print(f"before k_ls = {k_ls}")

def f():
    for i in range(1, 10):
        for j in range(3):
            # k_ls = np.append(k_ls, [1])   # syntax error
            k_ls[0] += 1

f()
print(k_ls)
print(sum(k_ls))

print(bin(10))
