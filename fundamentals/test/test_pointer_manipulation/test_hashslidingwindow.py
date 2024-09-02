from fundamentals.dsalgo.slidingwindow import maxuniquesubarray as mus

def test_maxUniqueSubarraySum():
    nums = [5, 3, 5, 1, 4, 8, 9]
    assert mus.maxUniqueSubarraySum(nums) == 30

if __name__ == "__main__":
    test_maxUniqueSubarraySum()