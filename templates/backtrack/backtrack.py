def reachleaf():
    return True

def isvalid(candidates, target):
    return True

def backtrack(candidates, target, s, path, ans):
    if reachleaf():         # reach the leaf node
        ans.append(path[:])
    for i in range(s, len(candidates)):
        if isvalid(candidates, target):
            path.append(candidates[:i + 1])
            backtrack() # adjust candidates, target as problem requires
            path.pop()
