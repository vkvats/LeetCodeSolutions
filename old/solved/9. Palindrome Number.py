class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x
        if x < 0:
            return False
        else: 
            value = 0
            while x > 0:
                a = x%10
                value = value*10 + a
                x = x//10
            if value == num:
                return True
            else:
                return False
