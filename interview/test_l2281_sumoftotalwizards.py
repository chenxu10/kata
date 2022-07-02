"""
As the ruler of a kingdom, you have an army of wizards at your command.

You are given a 0-indexed integer array strength, where strength[i] denotes the strength of the ith wizard. For a contiguous group of wizards (i.e. the wizards' strengths form a subarray of strength), the total strength is defined as the product of the following two values:

The strength of the weakest wizard in the group.
The total of all the individual strengths of the wizards in the group.
Return the sum of the total strengths of all contiguous groups of wizards. Since the answer may be very large, return it modulo 109 + 7.

A subarray is a contiguous non-empty sequence of elements within an array.

Input: strength = [5,4,6]
Output: 213
Explanation: The following are all the contiguous groups of wizards: 
- [5] from [5,4,6] has a total strength of min([5]) * sum([5]) = 5 * 5 = 25
- [4] from [5,4,6] has a total strength of min([4]) * sum([4]) = 4 * 4 = 16
- [6] from [5,4,6] has a total strength of min([6]) * sum([6]) = 6 * 6 = 36
- [5,4] from [5,4,6] has a total strength of min([5,4]) * sum([5,4]) = 4 * 9 = 36
- [4,6] from [5,4,6] has a total strength of min([4,6]) * sum([4,6]) = 4 * 10 = 40
- [5,4,6] from [5,4,6] has a total strength of min([5,4,6]) * sum([5,4,6]) = 4 * 15 = 60
The sum of all the total strengths is 25 + 16 + 36 + 36 + 40 + 60 = 213.

"""
from itertools import accumulate

def find_next_small_on_left(A):
    """
    Find the first index on the left side where A[i] > A[left]
    >>> find_left_index([1,3,2,9])
    [-1,0,0,2]
    """
    n = len(A)
    stack = []
    left = [-1] * n

    for i in range(n - 1, -1, -1):
        while stack and A[stack[-1]] >= A[i]:
            left[stack.pop()] = i
        stack.append(i)

    return left

def find_next_small_on_right(A):
    n = len(A)
    stack = []
    right = [n] * n

    for i in range(n):
        while stack and A[stack[-1]] > A[i]:
            right[stack.pop()] = i
        stack.append(i)
    
    return right

def totalStrength(A):
    n = len(A)
    left = find_next_small_on_left(A)
    right = find_next_small_on_right(A)

    print(left)
    print(right)

    res = 0
    acc = list(accumulate(accumulate(A), initial = 0))
    for i in range(n):
        l = left[i]
        r = right[i]
        lacc = acc[i] - acc[max(l,0)]
        racc = acc[r] - acc[i]
        ln = i - l
        rn = r - i
        res += A[i] * (racc * ln - lacc * rn)
    
    return res

def test_find_next_small_on_left():
    assert find_next_small_on_left([1,3,2,9]) == [-1,0,0,2]

def test_totalStrength():  
    assert totalStrength([1,2,1]) == 16

# Related Problems Leetcode 496

if __name__ == '__main__':
    test_totalStrength()