def maximum_consecutive_subsequence(arr):
    glabal_maximum = 0
    suffix_maximum = 0

    for i in range(len(arr) - 1):
        if suffix_maximum + arr[i] > glabal_maximum:
            suffix_maximum = suffix_maximum + arr[i]
            glabal_maximum = suffix_maximum
        else:
            if suffix_maximum + arr[i] > 0:
                suffix_maximum = suffix_maximum + arr[i]
            else:
                suffix_maximum = 0
    return glabal_maximum

def test_maximum_consecutive_subsequence():
    assert maximum_consecutive_subsequence(
        [2,-3,1.5,-1,3,-2]) == 3.5

if __name__ == '__main__':
    test_maximum_consecutive_subsequence()