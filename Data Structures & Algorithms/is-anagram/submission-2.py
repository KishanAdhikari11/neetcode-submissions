class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #sort and check 
        return sorted(s)==sorted(t)
        