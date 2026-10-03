class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        fp = 0

        for char in t:
            if fp == len(s):
                return True

            if char == s[fp]:
                fp += 1

        return fp == len(s)
        
        