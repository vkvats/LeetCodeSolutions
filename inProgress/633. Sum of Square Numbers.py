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

# Best solution from leetcode
#https://en.wikipedia.org/wiki/Sum_of_two_squares_theorem
def judgeSquareSum(self, c: int) -> bool:
    i=2
    while i*i < c:
        count = 0
        if c%i == 0:
            while c%i == 0:
                count+=1
                c = c//i
            if i%4 == 3 and count%2!=0:
                return False
        i+=1
    return c%4!=3

if __name__ == '__main__':
    c = 6
    print(judgeSquareSum(c))