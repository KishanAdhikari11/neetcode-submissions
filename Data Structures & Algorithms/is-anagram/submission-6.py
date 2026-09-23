class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charCount=[0]*26
        for char in s:
            charCount[ord(char)-ord('a')] +=1
        for char in t:
            charCount[ord(char)-ord('a')] -=1
        for x in charCount:
            if x!=0:
                return False

        return True

        
        