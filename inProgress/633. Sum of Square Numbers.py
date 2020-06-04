def judgeSquareSumX(c):
    """time limit exceeded"""
    import math
    square_root = int(math.sqrt(c))
    for a in range(0, square_root +1):
        for b in range(0, square_root + 1):
            if int(a**2) + int(b**2) == c:
                # print(a,b)
                return True
    return False

def judgeSquareSum(c):
    import math
    square_root = int(math.sqrt(c))
    for a in range(square_root + 1):
        b = math.sqrt(c-a*a)
        if int(b)*1 == b*1:
            return True
    return False


if __name__ == '__main__':
    c = 6
    print(judgeSquareSum(c))