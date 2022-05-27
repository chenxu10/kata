"""
Given a string s and a dictionary of strings wordDict, 
return true if s can be segmented into a space-separated 
sequence of one or more dictionary words.

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
"""
from collections import deque

# Failure point
def wordbreak(s,worddict):
    # end start index to q
    wordict = set(worddict)
    visited = set()
    q = deque([0])

    while q:
        start = q.popleft()
        if start not in visited:
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in wordict:
                    q.append(end)
                    if end == len(s):
                        return True               
            visited.add(end)
    return False

def test_wordbreak():
    s = "applepenapple"
    worddict = ["apple","pen"]
    s1 = "catsandog"
    worddict2 = ["cats","dog","sand","and","cat"]
    assert wordbreak(s, worddict) == True
    assert wordbreak(s1, worddict2) == False

# Failure point in pipeline
# Forget to introduce new auxiliary elements to make its use possible
# Forget to scale this to different output requirements
    # - Add new to path
