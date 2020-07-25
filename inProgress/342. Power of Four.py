class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        flag = True
        while flag:
            if num ==0: return False
            if num == 1: return True
            if num % 4 != 0: return False
            else:
                num = num/4

# Solution from leetcode
class SolutionF1:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False
        while n%4 == 0:
            n /= 4
        return True if n==1 else False

# Solution from leetcode
# Using maths
class SolutionF2:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and n & (n-1) == 0 and (n - 1) % 3 == 0