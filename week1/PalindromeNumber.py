class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        p=s[::-1]
        if p==s:
            return True
        else:
            return False