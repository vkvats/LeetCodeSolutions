def checkPerfectNumber(num):
    import math
    if num <=0 or num == 1:
        return False
    sum = 0
    for factor in range(1, int(math.sqrt(num) + 1)):
        if num % factor ==0:
            fac1 = num/factor
            sum += factor + fac1
    return sum == 2*num

# 3rd best solution from leetcode
"""Explanation is given in descriptin of solution"""
def checkPerfectNumber3rd(num):
    if num < 2:
        return False
    primes = [2, 3, 5, 7, 13, 17, 19, 31]
    for prime in primes:
        if (2 ** (prime - 1)) * ((2 ** prime) - 1) == num:
            return True
    return False


if __name__ == '__main__':
    num = 1
    print(checkPerfectNumber(num))