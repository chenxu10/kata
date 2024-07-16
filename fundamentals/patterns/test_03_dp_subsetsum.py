def knapsack01(set, sum):
    n = len(set)
    dp = [[False for _ in range(sum + 1)] for _ in range(n + 1)]
    dp[0][0] = True

    for i in range(1, n + 1):
        dp[i][0] = True

    for j in range(1, sum + 1):
        dp[0][j] = False

    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if set[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = (dp[i - 1][j]) or (dp[i - 1][j - set[i - 1]])

    return dp[n][sum]

def test_dp_knapsack():
    assert knapsack01([0,2,0,4],6) == True
    assert knapsack01([0,2,3],5) == True
    assert knapsack01([2],2) == True
    assert knapsack01([],2) == False
    assert knapsack01([42],0) == True

if __name__ == '__main__':
    test_dp_knapsack()