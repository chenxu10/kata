def parlindrome_part(s):
    path = []
    ans = []
    def isvalid(substring):
        return substring == substring[::-1]
    
    def backtrack(s, path, ans):
        if len(s) == 0:
            ans.append(path[:])
        for i in range(len(s)):
            if isvalid(s[:i+1]):
                path.append(s[:i+1])
                backtrack(s[i+1:],path,ans)
                path.pop()
    
    backtrack(s, path, ans)
    return ans

def test_parlindrom_part():
    return parlindrome_part("aab")

if __name__ == "__main__":
    print(test_parlindrom_part())