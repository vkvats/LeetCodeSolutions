# New method
# bit manipulation
"""
How we can check that number is power of 4? Straightforward algorithm is to try to divide it
 by 4 and check if we have 1 after several divisions, but complexity of this approach will be
 O(log n). There is smarter way. To check that number is power of 4, we need to check 3 conditions:

Number is positive.
Number is power of 2.
This power of 2 is even power.
First condition is trivial. For the second condition we can use x&(x-1) trick, which removes
the last significant bit of binary representation, for example 11010 & 11001 = 11000. Number
is power of two if it have only one significant bit, that is after this operation it must be equal to zero.

The last part is a bit tricky. Hopefully if reached this step, we already know, that number
 is a power of 2, so we have not a lot of options left: 1, 10, 100, 1000, ... How we can
 distinguish one half of them (odd powers) from another half? The trick is to use binary
 mask m = 1010101010101010101010101010101. For even powers of 2 we have for example m&100 = 100,
  if we use odd power, for example m&1000 = 0.

Complexity: both time and space is O(1), and this is honest O(1), not O(32) or O(16).
"""
class Solution:
    def isPowerOfFour(self, num):
        return num > 0 and num & (num-1) == 0 and 0b1010101010101010101010101010101 & num == num

# Another good solution
# Solution from leetcode
# Using maths
class SolutionF2:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0 and (n - 1) % 3 == 0

# bit manipulation
# recurssively divinging and checking
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        while num:
            if num & 3 != 0:
                # least 3 significant bits
                if num ^ 1 == 0:
                    return True
                return False
            num >>= 2

        return False

# using properties of log
import math
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num > 0:
            return math.log(num, 4).is_integer()
        return False


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

