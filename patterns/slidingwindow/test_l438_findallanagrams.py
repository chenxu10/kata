"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

"""

from collections import Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        >>>findAnagrams("abcde","cde")
        2
        """        
        # select, sequence, and iteration
        
        np, ns = len(p), len(s)
        if ns < np:
            return []
        
        s_count = Counter()
        p_count = Counter(p)
        
        ans = []
        for i in range(ns):
            s_count[s[i]] += 1
            if i >= np:
                if s_count[s[i - np]] == 1:
                    del s_count[s[i - np]]
                else:
                    s_count[s[i - np]] -= 1
            if s_count == p_count:
                ans.append(i - np + 1)
                
        return ans

            