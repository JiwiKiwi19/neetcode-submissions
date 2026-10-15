class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum()).lower()
        
        l, r = 0, len(s) - 1

        while l < r:
            if s[l].lower() != s[r].lower():
                return False 
            else:
                r -= 1
                l += 1
        
        return True

