def is_valid(substring):
    if len(substring) == 0 and int(substring) == 0:
        return True
    if 0 < int(substring) <= 255:
        return True
    return False

def reach_leaf_node(path, s):
    return (len(path) == 4) and len("".join(path)) == len(s)

def restore_ip_address(s):
    def backtrack(candidates, path, ans):
        if reach_leaf_node(path, s):
            ans.append(".".join(path[:]))
        for i in range(1, len(candidates) + 1):
            if is_valid(candidates[:i]):
                path.append(candidates[:i])
                backtrack(candidates[i:], path, ans)
                path.pop()

    path = []
    ans = []
    backtrack(s, path, ans)
    return ans

def test_reached_leaf_node():
    assert reach_leaf_node(["255","255","11","135"],"25525511135") == True

def test_restoreip():
    assert restore_ip_address("25525511135") == ["255.255.11.135","255.255.111.35"]




