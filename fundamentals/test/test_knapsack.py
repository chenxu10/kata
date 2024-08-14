
from fundamentals.manbercreativemethod.knapsack_10 import knapsack

def test_knapsack():
    assert knapsack([3,4,10],9) == 7
    assert knapsack([3,4,2],9) == 9

test_knapsack()