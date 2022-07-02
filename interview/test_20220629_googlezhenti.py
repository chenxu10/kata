"""
generate
(1) sum to 12
(2) 1 can not be behind 3 even in cyclic scenario
(3) 2 can not behind 1
[3,3,3,3], [1,2,3,3,3]
"""
def generate_12sum_list():
    # Geometric
    def dfs(candidates, target, s, cur, res):
        def isvalid(i):
            notreach12 = (candidates[i] <= target)
            not1behind2 = not(len(cur) > 0 and cur[-1] == 1 and candidates[i] == 2)
            if notreach12 and not1behind2:
                return True

        if (target == 0) and not (cur[-1]==3 and cur[0]==1):
            res.append(cur[:])
            return
        for i in range(s, len(candidates)):
            if isvalid(i):
                cur.append(candidates[i])
                dfs(candidates, target - candidates[i], 0, cur, res)
                cur.pop() 
        
    res = []
    cur = []
    s = 0
    candidates = [1,2,3]
    dfs(candidates, 12, s, cur, res)
    return res
        

if __name__ == "__main__":
    print(generate_12sum_list())