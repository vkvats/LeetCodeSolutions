# new method
# using bit manipulation
class Solution:
    """
    For the binary representation from right to left(until we find the leftmost 1):
    if we meet 0, result += 1 because we are doing divide;
    if we meet 1, result += 2 because we first do "-1" then do a divide;
    only exception is the leftmost 1, we just do a "-1" and it becomse 0 already.
    """
    def numberOfSteps (self, num: int) -> int:
        digits = f'{num:b}'
        return digits.count('1') - 1 + len(digits)

def numberOfSteps(num):
    steps = 0
    while num > 0:
        if num % 2 != 0:
            num = num - 1
            steps += 1
        else:
            num /= 2
            steps += 1
    return steps

if __name__ == '__main__':
    num = 8
    print(Solution().numberOfSteps(num))