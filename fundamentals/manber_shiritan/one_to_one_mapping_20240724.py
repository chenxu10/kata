# The Problem:

# Tricks:
# Reduce the size of the problem by eliminating elements from a set. Therefore,
# we try to find the eaisiest way to remove an element without changing the conditions
# of the problem.

def max_subset(A, f):
    visited = set()

    def dfs(element):
        visited.add(element)
        next_element = f[element]
        
        # No two elements are mapped in the same element
        if next_element in visited:
            result = set()
        # Maps every element to another element of S
        else:
            result = dfs(next_element)

        result.add(element)
        visited.remove(element)
        return result

    max_set = set()
    for element in A:
        current_set = dfs(element)
        if len(current_set) > len(max_set):
            max_set = current_set

    return max_set

def main():
    A = {1, 2, 3, 4, 5}
    f = {1: 2, 2: 3, 3: 1, 4: 5, 5: 4}
    result = max_subset(A, f)
    print(result)    

if __name__ == '__main__':
    main()
