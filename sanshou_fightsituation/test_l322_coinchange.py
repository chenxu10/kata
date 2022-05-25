def coinChange(coins, amount):
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0 

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

def test_coinChange():
    assert coinChange([1,2,4],5) == 2

    # min([1,2,4],5) ([1,2,4], 5-4) + 1
    # dp = [float("inf")] * (amount + 1)
    # dp[0] = 0

    # # the fewest number of coins I need to make up that amount
    # for coin in coins:
    #     for i in range(coin, amount + 1):
    #         dp[i] = min(dp[i], 1 + dp[i - coin])

    # return dp[amount] if dp[amount] != float('inf') else -1

# Attention not focused on unknown