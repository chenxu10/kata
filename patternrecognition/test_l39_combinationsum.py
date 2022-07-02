
def combination_sum(candidates,target):
    ans = []
    path = []
    def traverse(s, path, ans, target, candidates):
        if target == 0:
            ans.append(path[:])
        
        for i in range(s, len(candidates)):
            if candidates[i] <= target:
                path.append(candidates[i])
                traverse(i, path, ans, target - candidates[i], candidates)
                path.pop()
    
    candidates.sort()
    traverse(0, path, ans, target, candidates)
    return ans

# No duplication code

def test_combinationsum():
    print(combination_sum([2,3,6,7],7))
    print(combination_sum([1,3,5],8))
    assert combination_sum([2,3,6,7],7) == [[2,2,3],[7]]
    assert combination_sum([1,3,5],8) == [[1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 3], [1, 1, 1, 5], [1, 1, 3, 3], [3, 5]]

# Details:
# No duplications(should be sorted first and recursive start index i instead of zero)

if __name__ == "__main__":
    test_combinationsum()