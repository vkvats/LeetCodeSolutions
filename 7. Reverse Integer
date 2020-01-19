class Solution:
    def reverse(self, x: int) -> int:
        number = abs(x)
        value = 0
        while number > 0 :
            a = number%10
            value = value*10 + a
            number = number//10
        if value > (2**31-1):
            return 0
        elif x < 0:
            return -1* value 
        return value
