def n_choose_2(term_count):
    cc = 0
    for i in range(1, term_count):
        # print(f"i = {i}, j = ", end='')
        print(f"new tits = {i}, old tits = ", end='')
        for j in range(i):
            cc += 1
            print(f"{j} ", end='')
        print()

    return cc


x = n_choose_2(10)
print(x)