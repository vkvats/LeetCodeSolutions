def isUglyX(num):
    """time limit exceeded"""
    number = num
    if num ==1:
        return True
    if num ==0:
        return False
    while num%2 ==0:
        num = num /2
    if int(num)==-1:
        return False
    for factor in range(3, 1+ number, 2):
        while num % factor ==0:
            num = num/factor
            if factor != 3:
                if factor != 5:
                    return False
    if int(num) ==1:
        return True
    else:
        return False

def isUgly(num):
    if num < 1: return False
    for x in [2, 3, 5]:
        while (num % x) == 0:
            num /= x
    return num == 1

# best solution from leetcode
"""handling one factor at a time """
def isUglyBest(self, num: int) -> bool:
    if num == 1:
        return True

    while num > 5 and num % 5 == 0:
        num = num // 5
    if num == 5:
        return True
    while num > 3 and num % 3 == 0:
        num = num // 3
    if num == 3:
        return True
    while num > 2 and num % 2 == 0:
        num = num // 2

    return num == 2




if __name__ == '__main__':
    num = -2147483648
    print(isUgly(num))