
def isPowerOfThree(n):
    if n == 0:
        return False
    while n% 3 ==0:
        n = n/3
    if n ==1:
        return True
    else:
        return False

# same approache but different way of writing the code
def isPowerOfThree1(self, n: int) -> bool:
    if n == 0:
        return n==1
    while n%3 == 0:
        n /= 3
    return n == 1

if __name__ == '__main__':
    n = -27
    print(isPowerOfThree(n))