from collections import Counter

def max_length_duplicate_contiguous(s):
    counter = Counter(s)
    max_length = max(counter.values())
    result = [char for char, count in counter.items() if count == max_length]
    return result   


assert max_length_duplicate_contiguous('aaaabbbbccc') == ['a','b']  # Should return ['a', 'b']
assert max_length_duplicate_contiguous('abcd') == ['a','b','c','d']  # Should return ['a', 'b', 'c', 'd']