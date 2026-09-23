class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped_s=""
        for char in s:
            if char.isalnum():
                stripped_s = stripped_s + char
        normal_s=stripped_s.lower()
        return normal_s[::-1]==normal_s

        

        