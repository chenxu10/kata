def sum_naturals(a, b):
    if b < a:
        return 0
    else:
        return a + sum_naturals(a + 1, b)

def test_sum_naturals():
    assert sum_naturals(1,4) == 10
    assert sum_naturals(1,9) == 45


def sum_pi():
    return 1/3 + 1/35 

def test_pisum():
    assert sum_pi(1,5) == 1/3 + 1/35