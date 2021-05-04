from pprint import pp


def cashier_algo(coins_type: list, amount: int):
    res = dict()
    balance = amount
    for coin in coins_type:
        coin_count = 1
        while coin * coin_count <= balance:
            coin_count += 1

        if coin * coin_count > balance:
            coin_count -= 1

        # record
        res[coin] = coin_count
        balance -= coin * coin_count

    return res


def cashier_algo_from_pseudo(coins_type: list, amount: int):
    res = dict()
    for i in range(len(coins_type)):
        d = 0
        while amount >= coins_type[i]:
            d += 1
            amount -= coins_type[i]

        res[coins_type[i]] = d

    return res


COINS = [25, 10, 5, 1]

x = cashier_algo_from_pseudo(COINS, 110)
pp(x)
