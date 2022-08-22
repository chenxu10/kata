def max_stock_price(prices, k):
    # Sliding window + Hashset
    l = 0
    ans = -1
    for r in range(k - 1, len(prices)):
        window = prices[l: r + 1]
        if (len(set(window)) == len(window)):
            tempsum = sum(window)
            ans = max(ans, tempsum)
        l += 1
    return ans

    # O(n)
    # O(k)
    

def test_max_stock_price():
    assert max_stock_price([1,2,3,4], k=2) == 7
    assert max_stock_price([1,2,7,7,4,3,6], k=3) == 14


# Related problems: Leetcode 209

if __name__ == "__main__":
    test_max_stock_price()