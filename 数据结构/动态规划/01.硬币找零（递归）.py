# 找零问题的递归解决方案   极其耗时间的一个方案
from time import process_time

coin_list = [1,5,10,25]

def make_change_1(coin_map,change):
    if change  in coin_map:
        return 1
    min_coin = float('inf')
    for coin in [c for c in coin_map if c < change]:
        num_coins = 1 + make_change_1(coin_map,change - coin)

    min_coin = min(min_coin, num_coins)
    return min_coin

# test
# make_change_1(coin_list,63)

#   对以上方案的改进  映射

def make_change_2(coin_value_list, change, known_results):
    min_coins = change
    if change in coin_value_list:
        known_results[change] = 1
        return 1
    elif known_results[change] > 0:
        return known_results[change]
    else:
        for i in [c for c in coin_value_list if c <= change]:
            num_coins = 1 + make_change_2(
                coin_value_list, change - i, known_results,
            )
            if num_coins < min_coins:
                min_coins = num_coins
            known_results[change] = min_coins
    return min_coins


print("Counting change 2")
start = process_time()
result = make_change_2([1, 5, 10, 25], 63, [0] * 64)
end = process_time()
print(f"result: {result}; calculated in {end - start:2.5g} sec")

# 动态规划
def make_change_3(coin_value_list, change, min_coins):
    for cents in range(change + 1):
        coin_count = cents
        for j in [c for c in coin_value_list if c <= cents]:
            if min_coins[cents - j] + 1 < coin_count:
                coin_count = min_coins[cents - j] + 1
        min_coins[cents] = coin_count
    return min_coins[change]


print("Counting change 3")
start = process_time()
result = make_change_3([1, 5, 10, 25], 63, [0] * 64)
end = process_time()
print(f"result: {result}; calculated in {end - start:2.5g} sec")

# 动态规划改进
def make_change_4(coin_value_list, change, min_coins, coins_used):
    for cents in range(change + 1):
        coin_count = cents
        new_coin = 1
        for j in [c for c in coin_value_list if c <= cents]:
            if min_coins[cents - j] + 1 < coin_count:
                coin_count = min_coins[cents - j] + 1
                new_coin = j
        min_coins[cents] = coin_count
        coins_used[cents] = new_coin
    return min_coins[change]


def print_coins(coins_used, change):
    coin = change
    while coin > 0:
        this_coin = coins_used[coin]
        print(this_coin, end=" ")
        coin = coin - this_coin
    print()


def main():
    amnt = 63
    clist = [1, 5, 10, 21, 25]
    coins_used = [0] * (amnt + 1)
    coin_count = [0] * (amnt + 1)

    print("Making change for {}".format(amnt), end=" ")
    print(
        "requires the following {} coins: ".format(
            make_change_4(clist, amnt, coin_count, coins_used),
        ),
        end="",
    )
    print_coins(coins_used, amnt)
    print("The used list is as follows:")
    print(coins_used)


main()






















































