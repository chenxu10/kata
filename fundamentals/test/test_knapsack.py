


def knapsack(weights, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + weights[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][capacity]

def test_knapsack():
    assert knapsack([3,4,10],9) == 7
    assert knapsack([3,4,2],9) == 9


test_knapsack()