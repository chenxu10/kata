"""
Given an input string (s) and a pattern (p), 
implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".


"cb" "?a"  --> "c"  False
"aba" "*" --> True
"aba" "*a" --> True
"""

def isMatch(s, p):  
    def remove_duplicate_stars(p: str) -> str:
        new_string = []
        for char in p:
            if not new_string or char != '*':
                new_string.append(char)
            elif new_string[-1] != '*':
                new_string.append(char)
        return ''.join(new_string)

    def helper(s,p):
        if (s, p) in dp:
            return dp[(s, p)]
        if p == s or p == '*':
            dp[(s, p)] = True
        elif p == '' or s == '':
            dp[(s, p)] = False      
        if s[0] == p[0] or (p[0] == '?'):
            dp[(s,p)] = helper(s[1:], p[1:])
        if p[0] == "*":
            dp[(s,p)] = helper(s[1:], p) or helper(s,p[1:])
        else:
            dp[(s, p)] = False
        return dp[(s,p)]
        
    dp = {}
    p = remove_duplicate_stars(p)
    return helper(s,p)    


def test_isMatch():
    s = "abc"
    p = "aaa"
    assert isMatch(s, p) == False










